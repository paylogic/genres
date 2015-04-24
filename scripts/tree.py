"""Print a nice tree of the genres."""

import sys
import json

def strike(text):
    result = u''
    for c in text:
        result += c
        if c not in (' ', "\t"):
            result += u'\u0336'
    return result


def tree(source):
    """Print a tree of the genres

    :param source: Source json filename.

    """
    with open(source) as f:
        genres = json.load(f)

    ecc_codes = []
    genres_by_ecc = {}
    errors = []
    for code, genre in genres.iteritems():
        genre['code'] = code
        genres_by_ecc[genre['ecc']] = genre

    for ecc in sorted(genres_by_ecc.keys()):
        line = u'{0}{1} ({2}) {3}'.format(
            ('\t' * ecc.count('.')),
            ecc,
            genres_by_ecc[ecc]['code'],
            genres_by_ecc[ecc]['name']
        )
        if genres_by_ecc[ecc].get('deprecated'):
            print strike(line)
        else:
            print line


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python {0} json_file".format(sys.argv[0])
        sys.exit(1)

    tree(sys.argv[1])
