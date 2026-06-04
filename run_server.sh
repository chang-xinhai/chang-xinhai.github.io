#!/usr/bin/env bash
set -euo pipefail

bundle exec ruby -e 'load Gem.bin_path("jekyll", "jekyll")' -- liveserve
