#!/bin/bash
# Build script for VIPER Sphinx Documentation Container (Linux/Mac)

echo "================================================"
echo "VIPER Sphinx Container - Build Script"
echo "================================================"
echo ""

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed or not in PATH"
    echo "Please install Docker from https://docs.docker.com/get-docker/"
    exit 1
fi

echo "Step 1: Building Sphinx documentation..."
echo "------------------------------------------------"
mkdir -p docs/_build/html

# Build documentation locally if sphinx-build is available
if command -v sphinx-build &> /dev/null; then
    echo "Building documentation with local Sphinx..."
    cd docs
    sphinx-build -b html . _build/html
    cd ..
    echo "Documentation built successfully!"
else
    echo "Sphinx not found locally. Will build in container..."
fi

echo ""
echo "Step 2: Building Docker image..."
echo "------------------------------------------------"
docker build -t viper-sphinx:latest .

if [ $? -ne 0 ]; then
    echo "ERROR: Docker build failed"
    exit 1
fi

echo ""
echo "================================================"
echo "Build completed successfully!"
echo "================================================"
echo ""
echo "To run the container:"
echo "  docker run -p 8080:8080 viper-sphinx:latest"
echo ""
echo "To use with your project:"
echo "  docker run -v \$(pwd):/project -p 8080:8080 viper-sphinx:latest"
echo ""
echo "Access documentation at: http://localhost:8080"
echo "================================================"
