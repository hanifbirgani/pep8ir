# -*- coding: utf-8 -*-

# -- Project information -----------------------------------------------------

project = 'Python PEP8 Persian Translation'
copyright = 'Hanif Birgani'
author = 'Hanif Birgani'

version = '1'

# -- General configuration ---------------------------------------------------

extensions = []

source_suffix = '.rst'
master_doc = 'index'
language = 'fa'
exclude_patterns = ['_*', 'CONTRIBUTORS.rst', 'Thumbs.db', '.DS_Store']
if tags.has('gettext/gettext'):
    exclude_patterns += ['translation.rst']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

html_theme = 'pep8ir'
html_theme_path = ['./themes']

# -- Options for sphinx-intl example

locale_dirs = ['locale/']   # po files will be created in this directory
# optional: avoid file concatenation in sub directories.
gettext_compact = False
