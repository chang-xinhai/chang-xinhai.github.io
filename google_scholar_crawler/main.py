from datetime import datetime, timezone
import json
import os
import time
import sys

from scholarly import scholarly, ProxyGenerator


def maybe_fill_publication(publication: dict) -> dict:
    """Fetch per-publication details when Scholar allows it."""
    if os.environ.get("FILL_PUBLICATION_DETAILS", "false").lower() != "true":
        return publication
    try:
        # A tiny delay helps avoid hammering Scholar during scheduled Actions.
        time.sleep(0.75)
        return scholarly.fill(publication)
    except Exception as exc:  # noqa: BLE001 - keep the crawler useful even if one paper fails.
        publication["detail_error"] = str(exc)
        return publication


def main() -> None:
    # Try to set up a proxy to avoid Scholar blocking GitHub Actions IPs.
    pg = ProxyGenerator()
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
        print("Using free proxies for Scholar access", file=sys.stderr)
    else:
        print("No free proxy available, using direct connection", file=sys.stderr)

    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    author: dict = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    author["updated"] = datetime.now(timezone.utc).isoformat()

    publications = {}
    for publication in author.get("publications", []):
        publication = maybe_fill_publication(publication)
        author_pub_id = publication.get("author_pub_id")
        if author_pub_id:
            publications[author_pub_id] = publication
    author["publications"] = publications

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    print(json.dumps({
        "name": author.get("name"),
        "updated": author.get("updated"),
        "citedby": author.get("citedby"),
        "hindex": author.get("hindex"),
        "publications": len(publications),
    }, indent=2))


if __name__ == "__main__":
    main()
