@echo off
REM Build script for VIPER Sphinx Documentation Container (Windows)

echo ================================================
echo VIPER Sphinx Container - Build Script
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
run_tests.bat
if %errorlevel% neq 0 (
    echo ERROR: Sphinx documentation build failed
    exit /b 1
)

echo.
echo Step 2: Building Docker image...
echo ------------------------------------------------
docker build -t viper-sphinx:latest .

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
echo   docker run -p 8080:8080 viper-sphinx:latest
echo.
echo To use with your project:
echo   docker run -v %cd%:/project -p 8080:8080 viper-sphinx:latest
echo.
echo Access documentation at: http://localhost:8080
echo ================================================
