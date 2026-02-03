#!/bin/sh
# Startup script for the Sphinx documentation container

echo "================================================"
echo "VIPER Sphinx Documentation Container"
echo "================================================"
echo ""
echo "Starting HTTP server on port ${DOCS_PORT:-8080}..."
echo ""
echo "Access the documentation at:"
echo "  http://localhost:${DOCS_PORT:-8080}"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================================"
echo ""

# Start Python HTTP server
exec python3 -m http.server ${DOCS_PORT:-8080} --bind 0.0.0.0
