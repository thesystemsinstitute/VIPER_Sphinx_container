@echo off
REM Setup local test environment for Sphinx documentation generation
REM This script creates a Python virtual environment using uv and installs all dependencies

echo ====================================
echo Creating Test Documentation Environment
echo ====================================
echo.

REM Check if uv is installed
where uv >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: uv is not installed or not in PATH
    echo Please install uv first: https://github.com/astral-sh/uv
    echo Or use: pip install uv
    exit /b 1
)

REM Create virtual environment with uv
echo Creating virtual environment 'test_docs' with uv...
uv venv test_docs
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)

echo.
echo Virtual environment created successfully.
echo.

REM Install packages from requirements-windows.txt
echo Installing packages from requirements-windows.txt...
echo This may take several minutes...
echo Note: Some packages will be skipped if they require C libraries (pygraphviz, etc.)
echo.

REM Install packages one by one to skip problematic ones
for /f "usebackq tokens=* delims=" %%a in ("requirements-windows.txt") do (
    set "line=%%a"
    setlocal enabledelayedexpansion
    REM Skip lines starting with # or empty lines
    if not "!line:~0,1!"=="#" (
        if not "!line!"=="" (
            echo Installing !line!...
            uv pip install "!line!" --python test_docs >nul 2>&1
            if errorlevel 1 (
                echo   - Skipped !line! ^(failed to install^)
            ) else (
                echo   - Installed !line!
            )
        )
    )
    endlocal
)

echo.
echo Verifying Sphinx installation...
call test_docs\Scripts\activate.bat
python -c "import sphinx; print(f'Sphinx {sphinx.__version__} installed successfully')"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Sphinx not installed correctly
    call test_docs\Scripts\deactivate.bat 2>nul
    exit /b 1
)
call test_docs\Scripts\deactivate.bat 2>nul

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo Virtual environment: test_docs
echo Packages installed from: requirements-windows.txt
echo (Full package list including Linux-only packages in: requirements.txt)
echo.
echo Next steps:
echo   1. Run 'run_test.bat' to generate documentation
echo   2. Check output in 'test_docs_results' folder
echo.

exit /b 0
