"""Fetch homepage metrics with one Scholar profile request, without paper crawling.

Metric selectors/order adapted from scholarly's AuthorParser._fill_indices
(Unlicense). See THIRD_PARTY_NOTICES.md for the pinned upstream source.
"""

import argparse
from datetime import datetime, timezone
import json
import logging
import os
from pathlib import Path
import re
import sys
import time
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup

LOG = logging.getLogger(__name__)
PROFILE_URL = "https://scholar.google.com/citations"
REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ScholarMetrics/1.0; +https://chang-xinhai.github.io/)"}
METRICS = ("citedby", "citedby5y", "hindex", "hindex5y", "i10index", "i10index5y")


class ScholarError(RuntimeError):
    """An unsuccessful fetch must never replace previously published metrics."""


def parse_profile(html, scholar_id):
    soup = BeautifulSoup(html, "html.parser")
    if soup.select_one('#gs_captcha_ccl, #captcha-form, .g-recaptcha, #recaptcha'):
        raise ScholarError("Google Scholar returned a CAPTCHA; no data was written.")
    name = soup.select_one('#gsc_prf_in')
    table = soup.select_one('#gsc_rsb_st')
    if not name or not name.get_text(strip=True) or table is None:
        raise ScholarError("Response is not a Scholar profile with a statistics table.")
    cells = table.select('td.gsc_rsb_std')
    if len(cells) != 6:
        raise ScholarError("Incomplete statistics table; refusing to publish partial data.")
    values = []
    for cell in cells:
        value = cell.get_text(strip=True).replace(',', '').replace('\u00a0', '').replace(' ', '')
        if not re.fullmatch(r'[0-9]+', value):
            raise ScholarError("Non-numeric Scholar metric; refusing to replace it with zero.")
        values.append(int(value))
    # The profile exposes All / Since YEAR pairs, in this order.
    labels = [row.find('td').get_text(' ', strip=True).lower()
              for row in table.select('tr') if row.select('td.gsc_rsb_std')]
    if labels != ['citations', 'h-index', 'i10-index']:
        raise ScholarError("Unexpected statistics row order; Scholar markup may have changed.")
    return {"scholar_id": scholar_id, "name": name.get_text(strip=True),
            **dict(zip(METRICS, values)), "source": "google-scholar"}


def fetch_profile(scholar_id, session=None):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', scholar_id):
        raise ScholarError("GOOGLE_SCHOLAR_ID must be a profile ID, not a URL.")
    client = session or requests.Session()
    for attempt in range(1, 3):
        LOG.info("Fetching Scholar profile %s (attempt %s/2)", scholar_id, attempt)
        started = time.monotonic()
        try:
            response = client.get(PROFILE_URL, params={"user": scholar_id, "hl": "en"},
                                  headers=REQUEST_HEADERS, timeout=(10, 20))
        except requests.RequestException as exc:
            # Do not log exception URLs: custom proxy credentials may be present.
            LOG.warning("Request failed after %.1fs: %s", time.monotonic() - started,
                        type(exc).__name__)
            if attempt == 2:
                raise ScholarError("Scholar network request failed twice; old data is unchanged.") from None
            time.sleep(5)
            continue
        LOG.info("Scholar HTTP %s in %.1fs", response.status_code, time.monotonic() - started)
        if response.status_code in (403, 429):
            raise ScholarError(f"Scholar blocked/rate-limited this connection (HTTP {response.status_code}); no retry or CAPTCHA solving attempted.")
        if response.status_code in (500, 502, 503, 504) and attempt == 1:
            time.sleep(5)
            continue
        if response.status_code != 200:
            raise ScholarError(f"Unexpected Scholar HTTP {response.status_code}.")
        final_url = urlparse(response.url)
        if final_url.hostname != 'scholar.google.com' or parse_qs(final_url.query).get('user') != [scholar_id]:
            raise ScholarError("Scholar redirected away from the requested profile.")
        data = parse_profile(response.content, scholar_id)
        data['updated'] = datetime.now(timezone.utc).isoformat()
        return data
    raise ScholarError("No Scholar data returned.")


def write_results(data, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        'gs_data.json': data,
        'gs_data_shieldsio.json': {"schemaVersion": 1, "label": "citations", "message": str(data['citedby'])},
    }
    for filename, payload in outputs.items():
        destination = output_dir / filename
        temporary = destination.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        temporary.replace(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).parent / 'results')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', stream=sys.stdout)
    try:
        scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
        if not scholar_id:
            raise ScholarError('GOOGLE_SCHOLAR_ID is not configured.')
        data = fetch_profile(scholar_id)
        write_results(data, args.output_dir)
    except (ScholarError, OSError) as exc:
        LOG.error('%s', exc)
        return 1
    LOG.info('Updated %s: citations=%s, h-index=%s, timestamp=%s',
             data['name'], data['citedby'], data['hindex'], data['updated'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
