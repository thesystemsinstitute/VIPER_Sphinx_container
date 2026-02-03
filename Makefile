# Makefile for Sphinx documentation container

.PHONY: help build run stop clean rebuild serve dev logs shell

# Default target
help:
	@echo "VIPER Sphinx Container - Available Commands"
	@echo "============================================="
	@echo ""
	@echo "Building:"
	@echo "  make build        - Build the Docker image"
	@echo "  make rebuild      - Rebuild without cache"
	@echo ""
	@echo "Running:"
	@echo "  make run          - Run container (serve docs)"
	@echo "  make dev          - Run with auto-rebuild"
	@echo "  make serve        - Same as run"
	@echo ""
	@echo "Management:"
	@echo "  make stop         - Stop running container"
	@echo "  make logs         - View container logs"
	@echo "  make shell        - Open shell in container"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make clean-all    - Clean everything including image"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs         - Build documentation locally"
	@echo "  make docs-pdf     - Build PDF documentation"
	@echo ""

# Build the Docker image
build:
	@echo "Building Docker image..."
	docker build -t viper-sphinx:latest .
	@echo "Build complete!"

# Rebuild without cache
rebuild:
	@echo "Rebuilding Docker image (no cache)..."
	docker build --no-cache -t viper-sphinx:latest .
	@echo "Rebuild complete!"

# Run container to serve documentation
run:
	@echo "Starting Sphinx documentation server..."
	@echo "Access at: http://localhost:8080"
	docker run -d --name viper-sphinx-docs -p 8080:8080 viper-sphinx:latest
	@echo "Container started! View logs with: make logs"

# Run with auto-rebuild for development
dev:
	@echo "Starting development server with auto-rebuild..."
	@echo "Access at: http://localhost:8000"
	docker run -d --name viper-sphinx-dev -p 8000:8000 \
		-v $$(pwd)/docs:/sphinx/docs \
		viper-sphinx:latest \
		sh -c "cd /sphinx/docs && sphinx-autobuild . _build/html --host 0.0.0.0 --port 8000"
	@echo "Dev server started! Changes will auto-reload."

# Alias for run
serve: run

# Stop running containers
stop:
	@echo "Stopping containers..."
	-docker stop viper-sphinx-docs 2>/dev/null || true
	-docker stop viper-sphinx-dev 2>/dev/null || true
	-docker rm viper-sphinx-docs 2>/dev/null || true
	-docker rm viper-sphinx-dev 2>/dev/null || true
	@echo "Containers stopped."

# View logs
logs:
	@echo "Viewing logs (Ctrl+C to exit)..."
	docker logs -f viper-sphinx-docs 2>/dev/null || \
	docker logs -f viper-sphinx-dev 2>/dev/null || \
	echo "No running container found."

# Open shell in container
shell:
	@echo "Opening shell in container..."
	docker run -it --rm viper-sphinx:latest /bin/sh

# Build documentation locally (if Sphinx installed)
docs:
	@echo "Building documentation..."
	@if command -v sphinx-build >/dev/null 2>&1; then \
		cd docs && sphinx-build -b html . _build/html; \
		echo "Documentation built in docs/_build/html/"; \
	else \
		echo "Sphinx not installed locally. Using container..."; \
		docker run --rm -v $$(pwd):/project viper-sphinx:latest \
			sphinx-build -b html /project/docs /project/docs/_build/html; \
	fi

# Build PDF documentation
docs-pdf:
	@echo "Building PDF documentation..."
	docker run --rm -v $$(pwd):/project viper-sphinx:latest \
		sphinx-build -b latex /project/docs /project/docs/_build/latex
	@echo "PDF built in docs/_build/latex/"

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf docs/_build
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Clean complete!"

# Clean everything including Docker image
clean-all: clean stop
	@echo "Removing Docker image..."
	-docker rmi viper-sphinx:latest 2>/dev/null || true
	@echo "Full clean complete!"

# Docker Compose commands
up:
	@echo "Starting with Docker Compose..."
	docker-compose up -d
	@echo "Services started!"

down:
	@echo "Stopping Docker Compose services..."
	docker-compose down
	@echo "Services stopped!"

# Generate documentation for a project
gen-docs:
	@if [ -z "$(PROJECT)" ]; then \
		echo "Usage: make gen-docs PROJECT=/path/to/project"; \
		exit 1; \
	fi
	@echo "Generating documentation for $(PROJECT)..."
	docker run --rm -v $(PROJECT):/project viper-sphinx:latest \
		sphinx-build -b html /project/docs /project/docs/_build/html
	@echo "Documentation generated!"

# Initialize a new Sphinx project
init-project:
	@if [ -z "$(PROJECT)" ]; then \
		echo "Usage: make init-project PROJECT=/path/to/project"; \
		exit 1; \
	fi
	@echo "Initializing Sphinx project in $(PROJECT)..."
	docker run --rm -it -v $(PROJECT):/project viper-sphinx:latest \
		sphinx-quickstart /project/docs
	@echo "Project initialized!"
