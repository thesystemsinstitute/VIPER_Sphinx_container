# Changelog

All notable changes to the KENSAI Sphinx Container project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-25

### Added

#### Container & Infrastructure
- Docker container based on Python 3.13 Alpine Linux
- Minimal footprint design for efficient deployment
- Multi-service Docker Compose configuration
- Automated build scripts for Windows (build.bat) and Linux/Mac (build.sh)
- Helper scripts (sphinx-helper.bat, sphinx-helper.sh) for common tasks
- Makefile with comprehensive automation targets
- .dockerignore for optimized builds

#### System Tools & Dependencies
- Graphviz for diagram generation
- pyan3 for Python call graph generation
- Build tools and compilers for package compilation
- Git for version control integration

#### Python Packages (80+)

**Core Documentation Tools:**
- Sphinx 7.0+ (main documentation generator)
- pdoc3 (API documentation generator)

**Sphinx Extensions (60+):**
- sphinx-autoapi (automatic API documentation)
- sphinx-autobuild (live reload)
- sphinx-copybutton (copy code blocks)
- myst-parser (Markdown support)
- nbsphinx (Jupyter notebook integration)
- sphinxcontrib-httpdomain (HTTP API docs)
- sphinxext-opengraph (social media metadata)
- sphinx-hoverxref (hover tooltips)
- sphinx-git (git integration)
- And 50+ more extensions

**Themes:**
- sphinx-rtd-theme (Read the Docs)
- sphinx-book-theme (Book style)
- furo (Modern clean design)
- pydata-sphinx-theme (PyData community)
- sphinx-material (Material Design)
- Plus additional theme options

**Graphviz & Diagram Tools:**
- graphviz (Python bindings)
- pydot (DOT language interface)
- gprof2dot (profiling to diagrams)
- graphviz2drawio (convert to Draw.io)
- fsmdot (finite state machines)

**Markdown Support:**
- markdown (Python implementation)
- markdown-it-py (CommonMark parser)
- enumerate-markdown
- flake8-markdown

#### Documentation

**Main Pages:**
- Comprehensive index/landing page
- Quick reference guide
- Complete package inventory with tables
- Installation and usage instructions

**Tutorials:**
- Sphinx basics tutorial (complete guide)
- Themes customization guide
- Extensions usage guide
- Package-specific tutorials (sphinx-copybutton, myst-parser)

**Examples:**
- Basic documentation example
- API documentation example
- Jupyter notebook integration example
- Graphviz diagrams example

**Features:**
- Cross-references throughout
- Embedded YouTube tutorial videos
- Code highlighting with copy buttons
- Professional RTD theme
- Full-text search
- Mobile responsive design
- Navigation sidebar
- Table of contents

#### Container Features
- Built-in Python HTTP server on port 8080
- Automatic documentation build on container creation
- Embedded documentation accessible via web browser
- Support for volume mounting to serve external projects
- Auto-rebuild mode for development
- Comprehensive logging

#### Build & Deployment
- Automated documentation generation during build
- Multi-stage build optimization
- Layer caching for faster rebuilds
- Cross-platform compatibility (Windows, Linux, Mac)
- Docker Compose support for orchestration

### Configuration
- Sphinx configuration optimized for documentation
- Multiple output format support (HTML, PDF, ePub)
- Extensive extension configuration
- Theme customization options
- Graphviz integration configured

### Documentation Structure
- Organized into logical sections
- Progressive disclosure of complexity
- Clear navigation paths
- Comprehensive cross-linking
- Professional formatting

### Developer Experience
- Simple build process
- One-command deployment
- Helper scripts for common tasks
- Makefile for automation
- Clear error messages
- Comprehensive README
- Project summary documentation

## [Planned] - Future

### Potential Enhancements
- Additional package-specific tutorials
- PDF generation with LaTeX support
- More theme examples
- CI/CD integration examples
- Version info display script
- Health check endpoint
- Multi-language documentation support
- Additional specialized plugins
- Performance optimizations
- Automated testing framework

---

## Release Notes

### Version 1.0.0 Notes

This is the initial release of the KENSAI Sphinx Container, providing a complete, 
production-ready environment for Sphinx documentation generation. The container includes:

- **80+ packages** carefully selected for comprehensive documentation needs
- **Complete documentation** with tutorials and examples
- **Cross-platform support** for Windows, Linux, and Mac
- **Easy deployment** with automated build scripts
- **Professional output** using modern themes and extensions

The container is designed to be used both standalone (for viewing embedded documentation) 
and as a tool (for generating documentation for your projects).

### Known Limitations

1. Some packages in requirements.txt may have name variations or may not exist on PyPI
2. PDF generation requires additional LaTeX packages (can be added)
3. Some specialized extensions may have additional dependencies
4. Container size is optimized but still substantial due to the number of packages

### Compatibility

- **Docker:** Requires Docker 20.10 or later
- **Operating Systems:** Windows 10+, Linux (any), macOS 10.15+
- **Python:** Uses Python 3.13 (latest)
- **Sphinx:** Version 7.0+

### Upgrade Path

To upgrade to a newer version:

```bash
# Pull new version
docker pull kensai-sphinx:latest

# Or rebuild from source
docker build --no-cache -t kensai-sphinx:latest .
```

---

## Contributing

See README.md for contribution guidelines.

## Links

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Sphinx Themes Gallery](https://sphinx-themes.org/)
