"""Genre messages extractor."""

import json


def extract_genres(fileobj, keywords, comment_tags, options):
    """Extract genre codes for the translation."""
    genres = json.load(fileobj)
    for lineno, key in enumerate(genres):
        # lineno, funcname, messages, comments
        yield lineno, None, key, []
