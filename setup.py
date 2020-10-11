# -*- coding: utf-8 -*-

import setuptools
import os

#--------------------------------------------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'pyaction', '__version__.py'), 'r', encoding='utf-8') as f:
    file_data = [i.replace('\n', '').replace('\'', '').split(' = ') for i in f.readlines()]
    about = {k: v for k, v in file_data}

def readme(logo_end_line=0):
    """Extracts the logo from README file before pushing to PyPi."""

    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = ''.join(fh.readlines()[logo_end_line:])

    return long_description

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 1 - Planning",
    "Natural Language :: English",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Information Technology"
]

requires = [
]

modules = [
    'pyaction.general.objects'
]

#--------------------------------------------------------------------------------------------------------------

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    packages=[about['__title__']],
    py_modules=modules,
    classifiers=classifiers,
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requires,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    project_urls={
        'Documentation': about['__url__'],
        'Source': about['__url__'],
    },
)

#--------------------------------------------------------------------------------------------------------------
