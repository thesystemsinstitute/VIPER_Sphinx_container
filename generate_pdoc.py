#!/usr/bin/env python3
"""
Generate pdoc3 documentation for all installed packages.
"""
import subprocess
import sys
import os
from pathlib import Path

def get_installed_packages():
    """Get list of installed packages."""
    result = subprocess.run(
        [sys.executable, '-m', 'pip', 'list', '--format=json'],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error getting package list: {result.stderr}")
        return []
    
    import json
    packages = json.loads(result.stdout)
    return [(pkg['name'], pkg['version']) for pkg in packages]

def generate_pdoc_for_package(package_name, output_dir):
    """Generate pdoc3 documentation for a package."""
    try:
        # Try to generate documentation
        result = subprocess.run(
            [sys.executable, '-m', 'pdoc', '--html', '--output-dir', output_dir, package_name],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return True
        else:
            print(f"  ⚠️  Could not generate docs for {package_name}: {result.stderr[:100]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"  ⏱️  Timeout generating docs for {package_name}")
        return False
    except Exception as e:
        print(f"  ❌ Error with {package_name}: {str(e)[:100]}")
        return False

def main():
    """Main function to generate all documentation."""
    # Use relative path from script location
    script_dir = Path(__file__).parent
    output_dir = script_dir / 'docs' / 'pdoc'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("Generating pdoc3 documentation for installed packages")
    print("=" * 60)
    
    packages = get_installed_packages()
    print(f"\nFound {len(packages)} installed packages")
    
    # Generate docs for all packages from requirements.txt
    target_packages = [
        # Core
        'sphinx', 'pdoc3',
        # Extensions
        'sphinx-charts', 'sphinx-confluence', 'sphinx-lint', 'sphinx-library',
        'sphinx2doxygen', 'sphinx-issues', 'sphinx-tagtoctree', 'sphinx-vhdl',
        'sphinx-c-autodoc', 'sphinx-theme', 'sphinx-refdoc', 'sphinx-gitref',
        'sphinx-autoschematics', 'sphinx-pyreverse', 'sphinx-uml',
        'sphinxcontrib-asyncio', 'sphinxcontrib-googlemaps', 'sphinx-kml',
        'sphinxnotes-fasthtml', 'sphinx-wagtail-theme', 'sphinx-diagrams',
        'btd.sphinx.graphviz', 'sphinx-tojupyter', 'sphinxcontrib-cadquery',
        'epub2sphinx', 'sphinx-autodoc-defaultargs', 'sphinx-autodoc-annotation',
        'sphinx-autodoc2-fern', 'sphinx-collapsible-autodoc', 'sphinx-autodoc-toml',
        'sphinx-automodapi', 'pytest-doctestplus', 'sphinx-copybutton',
        'sphinx-prompt', 'sphinxemoji', 'sphinx-favicon', 'myst-parser',
        'sphinxcontrib-httpdomain', 'sphinx-autobuild', 'sphinx-autoapi',
        'nbsphinx', 'nbsphinx-link', 'sphinx-jupyter-kernel', 'sphinx-notfound-page',
        'sphinx-version-warning', 'sphinx-hoverxref', 'sphinx-last-updated-by-git',
        'sphinx-git', 'sphinxext-opengraph', 'breathe', 'exhale', 'ansible-sphinx', 'invoke-sphinx',
        'sphinx-analytics', 'sphinx-apischema', 'sphinx-autoindex', 'sphinx-autofixture',
        'sphinx-autopackagesummary', 'sphinx-advanced', 'sphinx-changelog',
        # New API & Code Documentation packages
        'sphinx-jsonschema', 'sphinx-sql', 'pydeps', 'sphinx-needs',
        # New API & Web Documentation packages
        'sphinxcontrib-openapi', 'sphinxcontrib-redoc', 'sphinxcontrib-websupport',
        'sphinxcontrib-restbuilder',
        # New Code Examples & Interactive Content packages
        'sphinx-gallery', 'sphinx-codeautolink', 'sphinx-thebe',
        # New Database & Data Documentation packages
        'eralchemy2', 'sqlalchemy',
        # New Performance & Build Tools packages
        'sphinx-asdf',
        # New Testing & Quality packages
        'doc8', 'rstcheck', 'sphinxcontrib-spelling',
        # New Internationalization packages
        'sphinx-intl', 'sphinx-polyversion',
        # New Export & Format Support packages
        'rst2pdf', 'rinohtype', 'sphinxcontrib-katex', 'sphinxcontrib-bibtex',
        # New Version Control & Collaboration packages
        'sphinx-multiversion', 'sphinx-versions', 'sphinx-comments', 'sphinxcontrib-contentui',
        # New Cloud & Infrastructure packages
        'sphinx-terraform',
        # New Search & Navigation packages
        'sphinx-sitemap', 'sphinx-tags',
        # New Specialized Documentation packages
        'sphinx-argparse', 'sphinx-click', 'sphinxcontrib-typer',
        'sphinx-pydantic', 'sphinx-toolbox',
        # Themes
        'sphinx-rtd-theme', 'sphinx-book-theme', 'pydata-sphinx-theme', 'furo',
        'piccolo-theme', 'sphinx-material', 'sphinx-press-theme', 'karma-sphinx-theme',
        'sphinxawesome-theme', 'sphinx-immaterial',
        # Diagram tools
        'pyan3', 'graphviz', 'pydot', 'gprof2dot', 'graphviz2drawio',
        'python-markdown-graphviz', 'fsmdot', 'quickdiagrams', 'dtreeplt',
        'pyprojectviz', 'pylint', 'code2flow', 'snakeviz', 'pydeps',
        'diagrams', 'railroad-diagrams', 'blockdiag', 'nwdiag', 'N2G',
        'rptree', 'pinout',
        # SVG
        'svg.py',
        # Markdown
        'markdown', 'enumerate-markdown', 'flake8-markdown', 'markdown-it-py',
        # Utilities
        'requests', 'beautifulsoup4', 'lxml', 'jinja2', 'docutils'
    ]
    
    success_count = 0
    total = 0
    
    # Create a mapping of package names
    installed_pkg_dict = {pkg.lower().replace('-', '_').replace('.', '_'): (pkg, ver) 
                         for pkg, ver in packages}
    
    for target_pkg in target_packages:
        normalized = target_pkg.lower().replace('-', '_').replace('.', '_')
        
        if normalized in installed_pkg_dict:
            pkg_name, version = installed_pkg_dict[normalized]
            total += 1
            print(f"\n[{total}/{len(target_packages)}] Generating docs for {pkg_name} ({version})...")
            if generate_pdoc_for_package(normalized, str(output_dir)):
                success_count += 1
                print(f"  ✅ Success")
        else:
            print(f"\n⚠️  Package not installed: {target_pkg}")
    
    print("\n" + "=" * 60)
    print(f"Documentation generation complete!")
    print(f"Successfully generated: {success_count}/{total} packages")
    print(f"Output directory: {output_dir}")
    print("=" * 60)
    
    # Create an index.html
    index_path = output_dir / 'index.html'
    with open(index_path, 'w') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Package Documentation Index</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Python Package Documentation</h1>
    <p>Auto-generated API documentation using pdoc3</p>
    <ul>
""")
        
        # List all generated documentation directories
        for item in sorted(output_dir.iterdir()):
            if item.is_dir() and item.name != '__pycache__':
                f.write(f'        <li><a href="{item.name}/index.html">{item.name}</a></li>\n')
        
        f.write("""    </ul>
</body>
</html>
""")
    
    print(f"\nIndex created at: {index_path}")

if __name__ == '__main__':
    main()
