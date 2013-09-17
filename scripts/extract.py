"""Genre messages extractor."""

import json


def extract_genres(fileobj, keywords, comment_tags, options):
    """Extract genre codes for the translation."""
    genres = json.load(fileobj)
    for lineno, (key, genre) in enumerate(genres.iteritems()):
        # lineno, funcname, messages, comments
        yield lineno, None, key, [genre['name']]
