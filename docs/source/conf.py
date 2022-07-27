# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import sphinxcontrib.bibtex
import myst_parser
import sphinxcontrib.apa

# -- Project information

project = 'Clinically Oriented Psychology'
copyright = '2022, Justpsychiatry'
author = 'Justpsychiatry'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.apa'
]


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'myst',
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'justpsychiatry': ('https://justpsychiatry.co.uk/en/latest/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
