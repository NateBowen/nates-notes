# Configuration file for the Sphinx documentation builder.

import os

# -- Project information

project = "Nate's Notes"
copyright = '2022, Nate Bowen'
author = 'Nate Bowen'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.plantuml',
    'myst_parser'
]

myst_url_schemes = [
    "http",
    "https"
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


# PlantUML Setup

if os.environ.get("READTHEDOCS") != None:
    plantuml = 'java -jar /usr/share/plantuml/plantuml.jar'
else:
    plantuml = os.getenv('plantuml')
    # plantuml = 'java -jar plantuml.jar'



# plantuml = os.getenv('plantuml')
# print(plantuml)
# # TODO - Get Plantuml installed on build machine
