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

The scheduled workflow in `.github/workflows/google_scholar_crawler.yaml` expects the repository secret `GOOGLE_SCHOLAR_ID`. It writes generated JSON files to the `google-scholar-stats` branch, where the homepage can fetch citation data.

## Credits

This site keeps selected Jekyll/theme assets from the original academic homepage template stack, including Font Awesome, Academicons, and components inspired by Minimal Mistakes and Academic Pages. See `LICENSE` and vendored asset headers for license details.
