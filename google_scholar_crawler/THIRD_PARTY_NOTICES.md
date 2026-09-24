# Google Scholar metrics parser

The six statistics selectors and All / Since-year field mapping in `main.py`
are adapted from `AuthorParser._fill_indices` in
[scholarly](https://github.com/scholarly-python-package/scholarly/blob/b9bc1806bb566eeeb52c0c726c0ca4fb649eee0d/scholarly/author_parser.py#L108-L121),
revision `b9bc1806bb566eeeb52c0c726c0ca4fb649eee0d`.

Upstream is released under the Unlicense; its text is reproduced in
`LICENSE.scholarly.txt`. The request transport, strict validation, output handling,
and workflow integration are local adaptations. No Scholar transport/retry code,
proxy rotation, or CAPTCHA handling from scholarly is used.
