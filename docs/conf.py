# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# Configuration file for the Sphinx documentation builder.

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../source/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'documentation-test' # pylint: disable=invalid-name
copyright = '2024, Joonatan Tammisto' # pylint: disable=invalid-name disable=redefined-builtin
author = 'Joonatan Tammisto' # pylint: disable=invalid-name
release = '0.0.1' # pylint: disable=invalid-name

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.autoprogram']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # pylint: disable=invalid-name
html_static_path = ['_static']
