# Configuration file for the Sphinx documentation builder.
import os
import sys

# -- Project information -----------------------------------------------------
project = 'KENSAI Sphinx Container Documentation'
copyright = '2026, KENSAI'
author = 'KENSAI'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.graphviz',
    'myst_parser',
    'sphinx_copybutton',
    'sphinxemoji.sphinxemoji',
    'sphinx_charts.charts',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = 'KENSAI Sphinx Container'
html_short_title = 'Sphinx Container'
html_logo = None
html_favicon = None

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'titles_only': False,
}

# Make external links open in new tab
html_context = {
    'display_github': False,
}

# Custom JavaScript to make links open in new tab
html_js_files = [
    'custom.js',
]

# -- Extension configuration -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# Autosummary settings
autosummary_generate = False  # Don't auto-generate stub files
autosummary_imported_members = False

# Todo extension
todo_include_todos = True

# Graphviz
graphviz_output_format = 'svg'

# MyST Parser settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    "tasklist",
]
