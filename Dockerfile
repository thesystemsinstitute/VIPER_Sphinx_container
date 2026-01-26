# Sphinx Documentation Container
# Based on Python 3.13 Alpine for minimal footprint
FROM python:3.13-alpine

LABEL maintainer="KENSAI Sphinx Container"
LABEL description="Comprehensive Sphinx documentation generation container with Graphviz support"
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

# Create output directory for generated documentation
RUN mkdir -p /sphinx/docs/_build/html

# Build the documentation
WORKDIR /sphinx/docs
RUN sphinx-build -b html . _build/html || true

# Copy startup script
COPY start-server.sh /sphinx/
RUN chmod +x /sphinx/start-server.sh

# Expose port for HTTP server
EXPOSE 8080

# Set working directory to the built docs
WORKDIR /sphinx/docs/_build/html

# Start the HTTP server
CMD ["/sphinx/start-server.sh"]
