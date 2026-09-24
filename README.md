# Xinhai Chang | Personal Homepage

This repository hosts the source code for [chang-xinhai.github.io](https://chang-xinhai.github.io), the personal academic homepage of Xinhai Chang.

## Overview

The site is built with Jekyll and published through GitHub Pages. It contains:

- A landing page with biography, research interests, news, awards, experience, services, and photography links.
- A publication list driven by `_data/publications.yml` and rendered by `_includes/publication-list.html`.
- Lightweight WebP paper teasers under `images/papers/webp/`.
- An optional Google Scholar crawler workflow that publishes citation stats to the `google-scholar-stats` branch.
- Personal assets such as avatar, favicon files, WeChat QR code, CV, and paper PDFs.

## Repository Layout

```text
_config.yml                         Site metadata and author profile
_pages/about.md                     Homepage content
_data/navigation.yml                Top navigation anchors
_data/publications.yml              Publication metadata
_includes/publication-list.html     Publication card renderer
assets/                             Styles, scripts, fonts, and theme assets
images/avatar/                      Avatar and favicon assets
images/papers/webp/                 Compressed publication teaser images
docs/                               CV and linked paper PDFs
google_scholar_crawler/             Citation stats crawler used by GitHub Actions
scripts/                            Maintenance scripts
```

## Local Development

Install Ruby/Jekyll dependencies once:

```bash
bundle install
```

Start a local server:

```bash
bash run_server.sh
```

Then open [http://127.0.0.1:4000](http://127.0.0.1:4000). If `_config.yml` changes, restart the server so Jekyll reloads the configuration.

## Updating Content

- Homepage copy: edit `_pages/about.md`.
- Publications: edit `_data/publications.yml`.
- Navigation anchors: edit `_data/navigation.yml`.
- Site metadata/social links: edit `_config.yml`.
- Paper teaser images: keep source images in `images/papers/`, run `python3 scripts/convert_paper_teasers_to_webp.py` when WebP thumbnails need to be regenerated, and point publications to `images/papers/webp/<name>.webp`.

## Google Scholar Citation Data

The workflow in `.github/workflows/google_scholar_crawler.yaml` runs daily at 16:17 Asia/Shanghai and expects the repository secret `GOOGLE_SCHOLAR_ID`. It makes one request to the public Scholar profile and reads the All / Since-year citation, h-index, and i10-index cells. It does not paginate publications or fetch paper details. The selectors are adapted from the Unlicense-licensed `scholarly` parser; see `google_scholar_crawler/THIRD_PARTY_NOTICES.md`.

Only validated metrics receive a new UTC `updated` timestamp. Successful scheduled runs publish `gs_data.json` and `gs_data_shieldsio.json` to the existing `google-scholar-stats` branch with a normal commit (no force push). The website reads that JSON when opened, so publishing metrics does not require rebuilding the website. Per-paper citation updates remain disabled.

Requests have a 10-second connect and 20-second read timeout. Transient network/server errors get at most one retry; HTTP 403/429, CAPTCHA pages, incomplete metrics, and unexpected redirects fail immediately. Failed fetches never replace old data or its timestamp. At the owner's request, both workflow jobs tolerate failures at the workflow level to avoid failed-run email/web notifications for this optional card. Actual errors remain in the step logs and run summary; a green workflow status alone does **not** prove an update. Publishing requires a successfully validated and uploaded artifact. The homepage hides metrics older than 30 days. Scholar can still block cloud runners: this is a best-effort scraper, not an official Scholar API.

To diagnose or validate a change, manually run **Get Citation Data** in GitHub Actions with `publish` unchecked. The run summary records the metrics and last-success timestamp, and the `scholar-metrics` artifact contains the exact JSON. To refresh the live card manually, run on `main` with `publish` checked. Publishing is disabled on all other branches.

The optional `simulate_failure` input exercises the quiet failure path without a Scholar request or publication. This must leave the fetch job failed, the overall workflow successful, and the publish job skipped. No mail, messaging, or issue-creation action is configured. Account-wide notification preferences and the website's separate Pages deployment are not changed.

Local validation (writes only local JSON):

```bash
python -m pip install -r google_scholar_crawler/requirements.txt
python -m unittest discover -s google_scholar_crawler -p 'test_*.py' -v
GOOGLE_SCHOLAR_ID=NVxBzq4AAAAJ python google_scholar_crawler/main.py --output-dir /tmp/scholar-results
```

## Credits

This site keeps selected Jekyll/theme assets from the original academic homepage template stack, including Font Awesome, Academicons, and components inspired by Minimal Mistakes and Academic Pages. See `LICENSE` and vendored asset headers for license details.
