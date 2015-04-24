"""Genre messages extractor."""

import json


def extract_genres(fileobj, keywords, comment_tags, options):
    """Extract messages from for the translations.

    :param fileobj: the file-like object the messages should be extracted
                    from
    :param keywords: a list of keywords (i.e. function names) that should
                     be recognized as translation functions
    :param comment_tags: a list of translator tags to search for and
                         include in the results
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)``
             tuples
    :rtype: ``iterator``
    """
    genres = json.load(fileobj)
    for lineno, (key, genre) in enumerate(genres.iteritems()):
        # lineno, funcname, messages, comments
        yield lineno, None, key, [genre['name']]
