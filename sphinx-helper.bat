@echo off
REM Quick usage helper for VIPER Sphinx Container (Windows)

if "%1"=="" goto help
if "%1"=="help" goto help
if "%1"=="build" goto build
if "%1"=="run" goto run
if "%1"=="stop" goto stop
if "%1"=="dev" goto dev
if "%1"=="shell" goto shell
if "%1"=="clean" goto clean
goto help

:help
echo.
echo VIPER Sphinx Container - Quick Commands
echo =========================================
echo.
echo Usage: sphinx-helper.bat [command]
echo.
echo Commands:
echo   test     - Build the local test docs
echo   build    - Build the Docker image
echo   run      - Run container and serve docs on port 8080
echo   dev      - Run with auto-rebuild on port 8000
echo   stop     - Stop running containers
echo   shell    - Open shell in container
echo   clean    - Clean build artifacts
echo   help     - Show this help
echo.
goto end

:test
echo Building local test docs...
call run_test.bat
if %errorlevel% equ 0 (
    echo.
    echo Build complete! open .\test_docs_results\index.html
)
goto end

:build
echo Building Docker image...
docker build -t viper-sphinx:latest .
if %errorlevel% equ 0 (
    echo.
    echo Build complete! Run with: sphinx-helper.bat run
)
goto end

:run
echo Starting Sphinx documentation server...
echo Access at: http://localhost:8080
docker run -d --name viper-sphinx-docs -p 8080:8080 viper-sphinx:latest
if %errorlevel% equ 0 (
    echo.
    echo Container started successfully!
    echo View logs: docker logs -f viper-sphinx-docs
)
goto end

:dev
echo Starting development server with auto-rebuild...
echo Access at: http://localhost:8000
docker run -d --name viper-sphinx-dev -p 8000:8000 -v %cd%/docs:/sphinx/docs viper-sphinx:latest sh -c "cd /sphinx/docs && sphinx-autobuild . _build/html --host 0.0.0.0 --port 8000"
if %errorlevel% equ 0 (
    echo.
    echo Dev server started! Changes will auto-reload.
)
goto end

:stop
echo Stopping containers...
docker stop viper-sphinx-docs 2>nul
docker stop viper-sphinx-dev 2>nul
docker rm viper-sphinx-docs 2>nul
docker rm viper-sphinx-dev 2>nul
echo Containers stopped.
goto end

:shell
echo Opening shell in container...
docker run -it --rm viper-sphinx:latest /bin/sh
goto end

:clean
echo Cleaning build artifacts...
if exist "docs\_build\" rmdir /s /q "docs\_build"
for /d /r %%i in (__pycache__) do @if exist "%%i" rmdir /s /q "%%i"
del /s /q *.pyc 2>nul
echo Clean complete!
goto end

:end
