# Configuration file for the Sphinx documentation builder.
import os
import sys

# Add examples directory to Python path for automodapi example
sys.path.insert(0, os.path.abspath('examples'))

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
    'sphinx_automodapi.automodapi',
    # 'sphinx_charts.charts',  # Disabled for Windows testing - requires sphinx_math_dollar
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

# Custom CSS
html_css_files = [
    'custom.css',
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

# -- Custom setup function to add line numbers to all code blocks -----------
def setup(app):
    """Add line numbers and language captions to all code blocks by default."""
    from sphinx.directives.code import CodeBlock
    from sphinx.directives.code import LiteralInclude
    
    # Store original run methods
    original_code_block_run = CodeBlock.run
    original_literal_include_run = LiteralInclude.run
    
    def code_block_run_with_enhancements(self):
        # Add linenos option if not explicitly set to False
        if 'linenos' not in self.options and 'no-linenos' not in self.options:
            self.options['linenos'] = True
            self.options['lineno-start'] = 1
        
        # Add caption with language if not already present
        if 'caption' not in self.options and 'name' not in self.options:
            language = self.arguments[0] if self.arguments else 'text'       
            self.options['caption'] = language
        
        return original_code_block_run(self)
    
    def literal_include_run_with_enhancements(self):
        # Add linenos option if not explicitly set to False
        if 'linenos' not in self.options and 'no-linenos' not in self.options:
            self.options['linenos'] = True
        
        # Add caption with language if not already present
        if 'caption' not in self.options and 'name' not in self.options:
            language = self.options.get('language', '')
            if language:
                self.options['caption'] = language
            else:
                # Try to guess from file extension
                filename = self.arguments[0] if self.arguments else ''
                if filename.endswith('.py'):
                    self.options['caption'] = 'Python'
                elif filename.endswith('.rst'):
                    self.options['caption'] = 'RST'
                elif filename.endswith('.js'):
                    self.options['caption'] = 'JavaScript'
                elif filename.endswith(('.yml', '.yaml')):
                    self.options['caption'] = 'YAML'
                elif filename.endswith(('.c', '.h')):
                    self.options['caption'] = 'C'
                elif filename.endswith(('.C', '.cpp', '.cxx', '.h', '.hpp', '.hxx')):
                    self.options['caption'] = 'C++'
                elif filename.endswith('.json'):
                    self.options['caption'] = 'JSON'
                else:
                    self.options['caption'] = 'Code'
        
        return original_literal_include_run(self)
    
    # Monkey patch the run methods
    CodeBlock.run = code_block_run_with_enhancements
    LiteralInclude.run = literal_include_run_with_enhancements
