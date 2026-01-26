# KENSAI Sphinx Documentation Container

A comprehensive Docker container for generating beautiful documentation using Sphinx, with an extensive collection of extensions, themes, and tools pre-installed.

## 🚀 Features

- **Python 3.13 Alpine** - Minimal footprint base image
- **80+ Sphinx Extensions** - Including autodoc, napoleon, autoapi, and more
- **Multiple Themes** - RTD, Furo, Book, PyData, Material, and others
- **Graphviz Support** - Create diagrams and flowcharts
- **Jupyter Integration** - Include notebooks in your docs
- **Markdown Support** - Write in Markdown or reStructuredText
- **Built-in Web Server** - Serve documentation on port 8080
- **Auto-rebuild** - Watch for changes and rebuild automatically
- **Comprehensive Documentation** - Includes tutorials and examples

## 📋 Prerequisites

- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- 2GB free disk space
- Internet connection for initial build

## 🏗️ Quick Start

### Windows

```batch
# Build the container
build.bat

# Run the container
docker run -p 8080:8080 kensai-sphinx:latest

# Access documentation at http://localhost:8080
```

### Linux/Mac

```bash
# Make build script executable
chmod +x build.sh

# Build the container
./build.sh

# Run the container
docker run -p 8080:8080 kensai-sphinx:latest

# Access documentation at http://localhost:8080
```

### Using Docker Compose

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## 📚 Using with Your Project

### Generate Documentation for Your Project

```bash
# Windows
docker run -v %cd%:/project kensai-sphinx sphinx-build /project/docs /project/docs/_build/html

# Linux/Mac
docker run -v $(pwd):/project kensai-sphinx sphinx-build /project/docs /project/docs/_build/html
```

### Serve Your Project Documentation

```bash
# Windows
docker run -p 8080:8080 -v %cd%:/project kensai-sphinx

# Linux/Mac
docker run -p 8080:8080 -v $(pwd):/project kensai-sphinx
```

### Auto-rebuild on Changes

```bash
# Windows
docker run -p 8000:8000 -v %cd%:/project kensai-sphinx ^
  sphinx-autobuild /project/docs /project/docs/_build/html ^
  --host 0.0.0.0 --port 8000

# Linux/Mac
docker run -p 8000:8000 -v $(pwd):/project kensai-sphinx \
  sphinx-autobuild /project/docs /project/docs/_build/html \
  --host 0.0.0.0 --port 8000
```

## 📦 Installed Packages

### Core Tools

- **Sphinx** - Documentation generator
- **pdoc3** - Auto-generate API documentation
- **Graphviz** - Graph visualization
- **pyan3** - Python call graph generator
- **60+ Diagram Tools** - diagrams, pyreverse, code2flow, blockdiag, nwdiag, railroad-diagrams, etc.
- **SVG Tools** - pytex2svg, svg-schematic, svg-plot, and more

### Sphinx Extensions (80+)

Complete list available in the container documentation at `/sphinx-packages`.

#### Popular Extensions:
- `sphinx-autoapi` - Automatic API documentation
- `sphinx-autobuild` - Live reload during development
- `sphinx-copybutton` - Copy buttons for code blocks
- `myst-parser` - Markdown support
- `nbsphinx` - Jupyter notebook integration
- `sphinxcontrib-httpdomain` - HTTP API documentation
- `sphinxext-opengraph` - Social media metadata
- `sphinx-hoverxref` - Hover tooltips

### Themes

- `sphinx-rtd-theme` - Read the Docs theme
- `sphinx-book-theme` - Book-style theme
- `furo` - Modern, clean theme
- `pydata-sphinx-theme` - PyData community theme
- `sphinx-material` - Material Design theme

### Additional Tools

- Markdown processors
- Graphviz Python bindings
- Code analysis tools
- 60+ diagram and visualization libraries
- SVG generation and manipulation tools

## 🎨 Customization

### Change Theme

Edit `docs/conf.py`:

```python
html_theme = 'furo'  # or 'sphinx_rtd_theme', 'sphinx_book_theme', etc.
```

### Enable Extensions

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx_copybutton',
    # Add more extensions
]
```

### Custom CSS

1. Create `docs/_static/custom.css`
2. Add to `conf.py`:

```python
html_static_path = ['_static']
html_css_files = ['custom.css']
```

## 📖 Documentation

The container includes comprehensive documentation:

- **Getting Started** - Introduction and setup
- **Sphinx Basics** - Core concepts and usage
- **Themes Guide** - Available themes and customization
- **Extensions Guide** - Using extensions effectively
- **Examples** - Practical examples and templates
- **Package Reference** - All installed packages with links

Access at `http://localhost:8080` after running the container.

## 🔧 Advanced Usage

### Build Different Formats

```bash
# PDF (requires LaTeX)
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-build -b latex /project/docs /project/docs/_build/latex

# ePub
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-build -b epub /project/docs /project/docs/_build/epub

# Man pages
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-build -b man /project/docs /project/docs/_build/man
```

### Run Sphinx Commands

```bash
# Initialize new project
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-quickstart /project/docs

# Check for broken links
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-build -b linkcheck /project/docs /project/docs/_build/linkcheck

# Generate API docs
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-apidoc -o /project/docs/api /project/src
```

### Environment Variables

- `DOCS_PORT` - Web server port (default: 8080)
- `PYTHONUNBUFFERED` - Python output buffering
- `PIP_NO_CACHE_DIR` - Disable pip cache

## 📁 Project Structure

```
KENSAI_Sphinx_container/
├── Dockerfile              # Container definition
├── docker-compose.yml      # Compose configuration
├── requirements.txt        # Python packages
├── build.bat              # Windows build script
├── build.sh               # Linux/Mac build script
├── start-server.sh        # Server startup script
├── docs/                  # Documentation source
│   ├── conf.py           # Sphinx configuration
│   ├── index.rst         # Main page
│   ├── sphinx-packages.rst
│   ├── tutorials/        # Tutorial pages
│   ├── examples/         # Example pages
│   ├── _static/          # Static files
│   ├── _templates/       # Custom templates
│   └── _build/           # Generated output
└── README.md             # This file
```

## 🐛 Troubleshooting

### Container Build Fails

```bash
# Clean build (no cache)
docker build --no-cache -t kensai-sphinx:latest .
```

### Port Already in Use

```bash
# Use different port
docker run -p 9090:8080 kensai-sphinx:latest
```

### Permission Issues (Linux)

```bash
# Run with current user
docker run --user $(id -u):$(id -g) -v $(pwd):/project kensai-sphinx
```

### Missing Packages

Add to `requirements.txt` and rebuild:

```bash
# Edit requirements.txt
echo "your-package-name" >> requirements.txt

# Rebuild
docker build -t kensai-sphinx:latest .
```

## 🔗 Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Sphinx Themes Gallery](https://sphinx-themes.org/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Graphviz Documentation](https://graphviz.org/)
- [Docker Documentation](https://docs.docker.com/)

## 📝 Examples

### Creating a Simple Project

```bash
# Initialize
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-quickstart /project/docs

# Edit docs/index.rst with your content

# Build
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-build /project/docs /project/docs/_build/html

# Serve
docker run -p 8080:8080 -v $(pwd):/project kensai-sphinx
```

### Python API Documentation

```bash
# Generate API docs from source
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-apidoc -f -o /project/docs/api /project/src

# Build with autodoc
docker run -v $(pwd):/project kensai-sphinx \
  sphinx-build /project/docs /project/docs/_build/html
```

## 🤝 Contributing

Suggestions for improvements:

1. Fork the repository
2. Make your changes
3. Test the build
4. Submit a pull request

## 📄 License

This container configuration is provided as-is for documentation generation purposes.

## 🙏 Acknowledgments

- Sphinx development team
- Extension and theme developers
- Docker community
- Open source contributors

## 📧 Support

For issues or questions:

1. Check the container documentation at `http://localhost:8080`
2. Review the troubleshooting section
3. Consult official Sphinx documentation
4. Check Docker logs: `docker logs <container-id>`

## 🔄 Version History

- **1.0** - Initial release with comprehensive Sphinx ecosystem

---

**Built with ❤️ for the documentation community**
