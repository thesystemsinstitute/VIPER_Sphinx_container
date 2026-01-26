#!/bin/bash
# Quick usage helper for KENSAI Sphinx Container (Linux/Mac)

set -e

show_help() {
    echo ""
    echo "KENSAI Sphinx Container - Quick Commands"
    echo "========================================="
    echo ""
    echo "Usage: ./sphinx-helper.sh [command]"
    echo ""
    echo "Commands:"
    echo "  build    - Build the Docker image"
    echo "  run      - Run container and serve docs on port 8080"
    echo "  dev      - Run with auto-rebuild on port 8000"
    echo "  stop     - Stop running containers"
    echo "  shell    - Open shell in container"
    echo "  clean    - Clean build artifacts"
    echo "  help     - Show this help"
    echo ""
}

build_image() {
    echo "Building Docker image..."
    docker build -t kensai-sphinx:latest .
    echo ""
    echo "Build complete! Run with: ./sphinx-helper.sh run"
}

run_server() {
    echo "Starting Sphinx documentation server..."
    echo "Access at: http://localhost:8080"
    docker run -d --name kensai-sphinx-docs -p 8080:8080 kensai-sphinx:latest
    echo ""
    echo "Container started successfully!"
    echo "View logs: docker logs -f kensai-sphinx-docs"
}

run_dev() {
    echo "Starting development server with auto-rebuild..."
    echo "Access at: http://localhost:8000"
    docker run -d --name kensai-sphinx-dev -p 8000:8000 \
        -v "$(pwd)/docs:/sphinx/docs" \
        kensai-sphinx:latest \
        sh -c "cd /sphinx/docs && sphinx-autobuild . _build/html --host 0.0.0.0 --port 8000"
    echo ""
    echo "Dev server started! Changes will auto-reload."
}

stop_containers() {
    echo "Stopping containers..."
    docker stop kensai-sphinx-docs 2>/dev/null || true
    docker stop kensai-sphinx-dev 2>/dev/null || true
    docker rm kensai-sphinx-docs 2>/dev/null || true
    docker rm kensai-sphinx-dev 2>/dev/null || true
    echo "Containers stopped."
}

open_shell() {
    echo "Opening shell in container..."
    docker run -it --rm kensai-sphinx:latest /bin/sh
}

clean_artifacts() {
    echo "Cleaning build artifacts..."
    rm -rf docs/_build
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    echo "Clean complete!"
}

case "$1" in
    build)
        build_image
        ;;
    run)
        run_server
        ;;
    dev)
        run_dev
        ;;
    stop)
        stop_containers
        ;;
    shell)
        open_shell
        ;;
    clean)
        clean_artifacts
        ;;
    help|"")
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        show_help
        exit 1
        ;;
esac
