"""Genre JSON generation."""

import os
import json

from babel import support

import paylogic_genres


def export_genres(source, output):
    """Export the genres json for the 3rd parties.

    :param source: Source json filename.
    :param output: Result json filename.

    """
    with open(source) as f:
        genres = json.load(f)

    result = {}
    for code, genre in genres.iteritems():
        item = {
            'name': {},
            'ecc': genre['ecc']
        }
        if 'parent' in genre:
            item['parent'] = genre['parent']
        result[code] = item

    # Generate the i18n genre names
    locale_dir = os.path.join(os.path.dirname(paylogic_genres.__file__), 'locale')
    english = support.Translations.load(locale_dir, locales=('en', ), domain='django')
    for lang in paylogic_genres.get_supported_languages():
        trans = support.Translations.load(locale_dir, locales=(lang, ), domain='django')
        for code, genre in result.iteritems():
            translated = trans.ugettext(code)
            # Fallback to english
            if lang != 'en' and translated == code:
                translated = english.ugettext(code)
            genre['name'][lang] = translated

    with open(output, 'w') as f:
        json.dump(result, f, indent=4)
