# Configuration file for the Sphinx documentation builder

import os
import sys

sys.path.append(os.path.abspath('../../src'))

from colorwheels import __version__
version = __version__

# -- Project information -----------------------------------------------------

project = 'colorwheels'
copyright = '2021, Quantum Spaces'
author = 'Quantum Quommander'

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon', 
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# adding RTD theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]
