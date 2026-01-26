# Build Instructions

Step-by-step guide to build and verify the KENSAI Sphinx Container.

## Prerequisites

### Required Software

1. **Docker**
   - **Windows:** [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - **Linux:** [Docker Engine](https://docs.docker.com/engine/install/)
   - **Mac:** [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)

2. **Minimum System Requirements**
   - 4GB RAM (8GB recommended)
   - 5GB free disk space
   - Internet connection (for initial build)

### Verify Docker Installation

```bash
# Check Docker version (should be 20.10 or later)
docker --version

# Check Docker is running
docker ps
```

## Build Methods

### Method 1: Using Build Scripts (Recommended)

#### Windows

```batch
# Open Command Prompt or PowerShell in project directory
cd c:\DATA\__PRJ\KENSAI_Sphinx_container

# Run build script
build.bat

# Wait for completion (may take 5-15 minutes on first build)
```

#### Linux/Mac

```bash
# Navigate to project directory
cd /path/to/KENSAI_Sphinx_container

# Make script executable
chmod +x build.sh

# Run build script
./build.sh

# Wait for completion (may take 5-15 minutes on first build)
```

### Method 2: Using Docker Directly

```bash
# Navigate to project directory
cd /path/to/KENSAI_Sphinx_container

# Build the image
docker build -t kensai-sphinx:latest .

# This will:
# 1. Download base image (Python 3.13 Alpine)
# 2. Install system dependencies
# 3. Install 80+ Python packages
# 4. Build documentation
# 5. Configure web server
```

### Method 3: Using Docker Compose

```bash
# Build with Docker Compose
docker-compose build

# Or build and start
docker-compose up -d
```

### Method 4: Using Makefile (Linux/Mac)

```bash
# Using Make
make build

# Or for clean build
make rebuild
```

## Build Process Details

### What Happens During Build

1. **Base Image Download** (~50MB)
   - Python 3.13 Alpine Linux

2. **System Dependencies** (~100MB)
   - Graphviz
   - Build tools
   - Development libraries

3. **Python Packages** (~200-300MB)
   - Sphinx and extensions
   - Themes
   - Tools and utilities
   - Total: 80+ packages

4. **Documentation Build**
   - Sphinx processes RST files
   - Generates HTML output
   - Creates search index

5. **Configuration**
   - Sets up startup script
   - Configures HTTP server
   - Exposes port 8080

### Expected Build Time

- **First build:** 5-15 minutes (depends on internet speed)
- **Subsequent builds:** 1-3 minutes (with layer caching)
- **Clean rebuild:** 5-15 minutes

### Expected Image Size

- **Final image:** ~500-700MB
- **Base image:** ~50MB
- **Dependencies:** ~450-650MB

## Verify Build

### 1. Check Image Created

```bash
# List Docker images
docker images | grep kensai-sphinx

# Should show:
# REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
# kensai-sphinx   latest    <id>           <time>          ~600MB
```

### 2. Run Container

```bash
# Start container
docker run -d --name test-sphinx -p 8080:8080 kensai-sphinx:latest

# Check container is running
docker ps | grep test-sphinx

# Should show container with STATUS "Up"
```

### 3. Check Logs

```bash
# View container logs
docker logs test-sphinx

# Should show:
# ================================================
# KENSAI Sphinx Documentation Container
# ================================================
# 
# Starting HTTP server on port 8080...
```

### 4. Access Documentation

1. Open web browser
2. Navigate to: http://localhost:8080
3. You should see the KENSAI Sphinx Container documentation

**Expected:**
- Title: "KENSAI Sphinx Documentation Container"
- Navigation sidebar on left
- Main content area
- Search box
- Links to tutorials and examples

### 5. Test Documentation Features

**Check Navigation:**
- Click "Quick Reference" in sidebar
- Click "Sphinx Packages" in sidebar
- Click "Tutorials" to expand
- Click "Examples" to expand

**Check Search:**
- Type "graphviz" in search box
- Should find multiple references
- Click a result to navigate

**Check Code Blocks:**
- Find any code block
- Hover over it
- Copy button should appear
- Click to copy

**Check Cross-References:**
- Click any internal link (e.g., `:doc:` links)
- Should navigate to referenced page
- Back button should work

### 6. Verify Package Installation

```bash
# Check installed packages
docker run --rm kensai-sphinx pip list | grep -i sphinx

# Should show many Sphinx packages

# Check specific package
docker run --rm kensai-sphinx pip show sphinx

# Should show Sphinx details
```

### 7. Test Documentation Generation

```bash
# Test Sphinx build command
docker run --rm kensai-sphinx sphinx-build --version

# Should show: sphinx-build 7.x.x

# Test with a sample project
docker run --rm -v $(pwd):/project kensai-sphinx \
  sphinx-build /project/docs /project/docs/_build/html

# Should build successfully
```

## Troubleshooting

### Build Fails

**Error: Cannot connect to Docker daemon**

```bash
# Check Docker is running
docker ps

# If not, start Docker Desktop (Windows/Mac) or Docker service (Linux)
```

**Error: No space left on device**

```bash
# Clean up Docker
docker system prune -a

# Remove unused images
docker image prune -a
```

**Error: Package installation fails**

```bash
# Try clean build
docker build --no-cache -t kensai-sphinx:latest .

# Or check internet connection
ping pypi.org
```

**Error: Build times out**

```bash
# Some packages may be slow to install
# Try building with more time or better internet connection

# Check specific package installation
docker build --progress=plain -t kensai-sphinx:latest .
```

### Container Won't Start

**Check logs:**

```bash
docker logs test-sphinx
```

**Port already in use:**

```bash
# Use different port
docker run -d -p 9090:8080 kensai-sphinx:latest

# Access at http://localhost:9090
```

**Permission errors (Linux):**

```bash
# Run as current user
docker run -d --user $(id -u):$(id -g) -p 8080:8080 kensai-sphinx:latest
```

### Documentation Not Accessible

**Check container is running:**

```bash
docker ps | grep kensai-sphinx
```

**Check port mapping:**

```bash
docker port <container-name>
```

**Try with explicit IP:**

```
http://127.0.0.1:8080
```

**Check firewall:**

- Ensure port 8080 is not blocked
- Try with different port

### Slow Build

**Use Docker BuildKit:**

```bash
# Enable BuildKit (Linux/Mac)
export DOCKER_BUILDKIT=1
docker build -t kensai-sphinx:latest .

# Windows PowerShell
$env:DOCKER_BUILDKIT=1
docker build -t kensai-sphinx:latest .
```

**Use build cache:**

```bash
# Subsequent builds should be much faster
# Only changed layers are rebuilt
```

## Clean Up After Testing

```bash
# Stop and remove test container
docker stop test-sphinx
docker rm test-sphinx

# Or keep for later use
docker stop test-sphinx
```

## Production Deployment

### Tag Image

```bash
# Tag with version
docker tag kensai-sphinx:latest kensai-sphinx:1.0.0
```

### Save Image

```bash
# Save to file
docker save kensai-sphinx:latest | gzip > kensai-sphinx-1.0.0.tar.gz

# Load on another machine
docker load < kensai-sphinx-1.0.0.tar.gz
```

### Push to Registry

```bash
# Tag for registry
docker tag kensai-sphinx:latest your-registry.com/kensai-sphinx:latest

# Push
docker push your-registry.com/kensai-sphinx:latest
```

## Validation Checklist

- [ ] Docker installed and running
- [ ] Build completes without errors
- [ ] Image appears in `docker images`
- [ ] Container starts successfully
- [ ] Port 8080 accessible
- [ ] Documentation loads in browser
- [ ] Navigation works
- [ ] Search works
- [ ] Code copy buttons work
- [ ] All tutorial pages load
- [ ] All example pages load
- [ ] Package list displays correctly
- [ ] Sphinx commands work
- [ ] Can generate docs for external project

## Next Steps

After successful build and verification:

1. **Read the documentation** at http://localhost:8080
2. **Try the quick reference** for common tasks
3. **Explore tutorials** to learn Sphinx features
4. **Test with your project** to generate documentation
5. **Customize** as needed for your requirements

## Support

- **Documentation:** http://localhost:8080 (when container is running)
- **README:** See [README.md](README.md)
- **Project Summary:** See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- **Changelog:** See [CHANGELOG.md](CHANGELOG.md)

## Build Metrics

After successful build, you should see approximately:

```
Image Size:         ~500-700 MB
Build Time:         5-15 minutes (first build)
Memory Usage:       ~100-200 MB (running)
CPU Usage:          Low (serving docs)
Packages Installed: 80+
Documentation Size: ~5-10 MB
```

## Success Criteria

Your build is successful when:

✅ `docker images` shows kensai-sphinx:latest
✅ Container starts without errors
✅ http://localhost:8080 shows documentation
✅ All navigation links work
✅ Search functionality works
✅ Code examples display correctly
✅ Can generate docs for test project

---

**Congratulations!** Your KENSAI Sphinx Container is ready to use.
