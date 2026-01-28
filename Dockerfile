# Sphinx Documentation Container
# Based on Python 3.13 Alpine for minimal footprint
FROM python:3.13-alpine

LABEL maintainer="KENSAI Sphinx Container"
LABEL description="Comprehensive Sphinx documentation generation container"
LABEL version="1.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DOCS_PORT=8080

# Install system dependencies
RUN apk add --no-cache \
    graphviz \
    graphviz-dev \
    doxygen \
    ttf-dejavu \
    build-base \
    gcc \
    musl-dev \
    linux-headers \
    git \
    && rm -rf /var/cache/apk/*

# Create working directory
WORKDIR /sphinx

# Copy requirements file
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy documentation source
COPY docs/ /sphinx/docs/

# Copy helper scripts
COPY generate_pdoc.py /sphinx/
COPY update_versions.py /sphinx/
COPY fix_doc_links.py /sphinx/
COPY validate_manual_links.py /sphinx/

# Update package versions in documentation
RUN python3 /sphinx/update_versions.py

# Validate and fix Manual links (remove broken URLs)
RUN python3 /sphinx/validate_manual_links.py

# Generate pdoc3 documentation for installed packages
RUN python3 /sphinx/generate_pdoc.py

# Fix documentation links (remove links for packages without generated docs)
RUN python3 /sphinx/fix_doc_links.py

# Create output directory for generated documentation
RUN mkdir -p /sphinx/docs/_build/html

# Build the documentation
WORKDIR /sphinx/docs
RUN sphinx-build -b html . _build/html || true

# Copy pdoc documentation to the build output
RUN cp -r /sphinx/docs/pdoc /sphinx/docs/_build/html/pdoc

# Copy startup script
COPY start-server.sh /sphinx/
RUN chmod +x /sphinx/start-server.sh

# Expose port for HTTP server
EXPOSE 8080

# Set working directory to the built docs
WORKDIR /sphinx/docs/_build/html

# Start the HTTP server
CMD ["/sphinx/start-server.sh"]
