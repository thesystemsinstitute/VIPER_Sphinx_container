# Configuration file for the Sphinx documentation builder.
import os
import sys

# Add project root and tutorials/packages to Python path
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('tutorials/packages'))

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
    'sphinxcontrib.httpdomain',
    'sphinx_prompt',
    'sphinx_pyreverse',
    # 'sphinx_charts.charts',  # Disabled for Windows testing - requires sphinx_math_dollar
]

# Optional legacy extension: sphinx_kml may be incompatible with newer Sphinx
KML_AVAILABLE = False
try:
    import sphinx_kml  # noqa: F401
    extensions.append('sphinx_kml')
    KML_AVAILABLE = True
except Exception:
    KML_AVAILABLE = False

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
    from collections import defaultdict
    from docutils import nodes
    from docutils.parsers.rst import Directive
    from docutils.parsers.rst import directives
    from docutils.parsers.rst import roles
    def _any_option_spec():
        return defaultdict(lambda: directives.unchanged)

    class LiteralBlockDirective(Directive):
        has_content = True
        optional_arguments = 1
        final_argument_whitespace = True
        option_spec = _any_option_spec()

        def run(self):
            text = '\n'.join(self.content)
            return [nodes.literal_block(text, text)]

    class FileLiteralDirective(Directive):
        required_arguments = 1
        optional_arguments = 10
        final_argument_whitespace = True
        has_content = True
        option_spec = _any_option_spec()

        def run(self):
            text = self.arguments[0]
            return [nodes.literal_block(text, text)]

    def generic_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        options = options or {}
        node = nodes.literal(text, text)
        return [node], []

    if not KML_AVAILABLE:
        app.add_directive('kml', LiteralBlockDirective)
        app.add_directive('kml-file', FileLiteralDirective)
        app.add_directive('kml-download', FileLiteralDirective)
        app.add_directive('kml-export', LiteralBlockDirective)

    # Fallback directives for optional extensions
    app.add_directive('schematic', LiteralBlockDirective)
    app.add_directive('chart', FileLiteralDirective)
    app.add_directive('diagrams', LiteralBlockDirective)
    app.add_directive('pyreverse', LiteralBlockDirective)
    app.add_directive('refdoc', LiteralBlockDirective)
    app.add_directive('refdoc-module', LiteralBlockDirective)
    app.add_directive('refdoc-package', LiteralBlockDirective)
    app.add_directive('refdoc-index', LiteralBlockDirective)
    app.add_directive('git_changelog', LiteralBlockDirective)
    app.add_directive('gitlog', LiteralBlockDirective)
    app.add_directive('gitcompare', LiteralBlockDirective)
    app.add_directive('gitcontributors', LiteralBlockDirective)
    app.add_directive('gitblame', LiteralBlockDirective)
    app.add_directive('gitstats', LiteralBlockDirective)
    app.add_directive('gitcurrent', LiteralBlockDirective)
    app.add_directive('gitbuildinfo', LiteralBlockDirective)
    app.add_directive('gitreleasenotes', LiteralBlockDirective)
    app.add_directive('gitchangelog', LiteralBlockDirective)
    app.add_directive('gitsubmodule', LiteralBlockDirective)
    app.add_directive('grid', LiteralBlockDirective)

    # Fallback roles for optional extensions
    roles.register_local_role('gitrepo', generic_role)
    roles.register_local_role('gitcommit', generic_role)
    roles.register_local_role('gitbranch', generic_role)
    roles.register_local_role('gittag', generic_role)
    roles.register_local_role('gitfile', generic_role)
    roles.register_local_role('gitpr', generic_role)
    roles.register_local_role('gitmr', generic_role)
    roles.register_local_role('gitauthor', generic_role)
    roles.register_local_role('issue', generic_role)
    roles.register_local_role('pr', generic_role)
    roles.register_local_role('user', generic_role)
    roles.register_local_role('commit', generic_role)
    roles.register_local_role('refdoc', generic_role)
    
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
