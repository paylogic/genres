"""Genre JSON checking."""

import sys
import json


def check_json(source):
    """Check the json for issues in relation to parents not existing and ecc codes duplicates.

    :param source: Source json filename.

    """
    with open(source) as f:
        genres = json.load(f)

    ecc_codes = []
    check_later = []
    codes = {}
    errors = []
    for code, genre in genres.iteritems():
        codes[code] = genre['ecc']
        if genre['ecc'] in ecc_codes:
            errors.append('Genre {0} has duplicate ecc code found: {1}'.format(code, genre['ecc']))
        else:
            ecc_codes.append(genre['ecc'])

        if 'parent' in genre and genre['parent'] not in codes:
            check_later.append((genre['parent'], genre['ecc']))

    for (code, ecc) in check_later:
        if code not in codes:
            errors.append('Genre {0} has invalid parent: {1}'.format(code, genre['parent']))
        elif not ecc.startswith(codes[code]):
            errors.append('Genre {0} has invalid ecc code for parent: {1} ({2})'.format(code, ecc, codes[code]))

    return errors


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python {0} json_file".format(sys.argv[0])
        sys.exit(1)

    errors = check_json(sys.argv[1])
    if len(errors):
        print "\n".join(errors)
        sys.exit(1)
    print "No errors found"
