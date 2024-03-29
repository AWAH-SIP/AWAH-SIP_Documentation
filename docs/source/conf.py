# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'AWAH-SIP'
copyright = '2023'
author = 'Adi Hilber, Andy Weiss'

release = '3.2'
version = '3.2'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Add/Update "html_theme_options" like this on your conf.py
html_theme_options = {'body_max_width': '90%'}
