@echo off
REM Build script for KENSAI Sphinx Documentation Container (Windows)

echo ================================================
echo KENSAI Sphinx Container - Build Script
echo ================================================
echo.

REM Check if Docker is available
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop from https://www.docker.com/products/docker-desktop
    exit /b 1
)

echo Step 1: Building Sphinx documentation...
echo ------------------------------------------------
if not exist "docs\_build" mkdir docs\_build
if not exist "docs\_build\html" mkdir docs\_build\html

REM Build documentation locally if sphinx-build is available
where sphinx-build >nul 2>&1
if %errorlevel% equ 0 (
    echo Building documentation with local Sphinx...
    cd docs
    sphinx-build -b html . _build\html
    cd ..
    echo Documentation built successfully!
) else (
    echo Sphinx not found locally. Will build in container...
)

echo.
echo Step 2: Building Docker image...
echo ------------------------------------------------
docker build -t kensai-sphinx:latest .

if %errorlevel% neq 0 (
    echo ERROR: Docker build failed
    exit /b 1
)

echo.
echo ================================================
echo Build completed successfully!
echo ================================================
echo.
echo To run the container:
echo   docker run -p 8080:8080 kensai-sphinx:latest
echo.
echo To use with your project:
echo   docker run -v %cd%:/project -p 8080:8080 kensai-sphinx:latest
echo.
echo Access documentation at: http://localhost:8080
echo ================================================
