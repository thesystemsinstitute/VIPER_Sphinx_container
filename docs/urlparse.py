"""Python 2 urlparse compatibility shim for legacy extensions."""

from urllib.parse import (
    urlparse,
    urlunparse,
    urljoin,
    urlsplit,
    urlunsplit,
    urldefrag,
    parse_qs,
    parse_qsl,
    urlencode,
    quote,
    quote_plus,
    unquote,
    unquote_plus,
)

__all__ = [
    "urlparse",
    "urlunparse",
    "urljoin",
    "urlsplit",
    "urlunsplit",
    "urldefrag",
    "parse_qs",
    "parse_qsl",
    "urlencode",
    "quote",
    "quote_plus",
    "unquote",
    "unquote_plus",
]
