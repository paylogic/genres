#!/usr/bin/env python

import os
from setuptools import setup, Command


class ExportJSON(Command):
    """Export i18n genres json."""

    user_options = []

    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        from scripts.export import export_genres
        dirname = os.path.dirname(__file__)
        export_genres(
            source=os.path.join(dirname, 'src', 'genres.json'),
            output=os.path.join(dirname, 'genres.json'),
        )


setup(
    name='paylogic-genres',
    description='Genre classification used by Paylogic.',
    #long_description=__doc__,
    author='Paylogic',
    license='MIT license',
    version='0.1.0',
    install_requires=[
        'babel',
        'transifex-client',
    ],
    cmdclass={
        'export_json': ExportJSON,
    },
    url='https://github.com/paylogic/genres',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    #tests_require=tests_require,
    entry_points={
        'babel.extractors': [
            'genres = scripts.extract:extract_genres',
        ],
    },
    packages=['paylogic_genres'],
    message_extractors={
        '': [
            ('paylogic_genres.json', 'genres', None),
        ],
    },
    package_data={
        '': [
            'locale/*/*/*',
        ]
    },
    data_files=[
        ('paylogic_genres', ['genres.json']),
    ],
)
