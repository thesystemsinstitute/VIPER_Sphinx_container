@echo off
REM Run Sphinx documentation generation using test environment
REM Generates HTML documentation into test_docs_results folder

echo ====================================
echo Running Sphinx Documentation Build
echo ====================================
echo.

REM Check if virtual environment exists
if not exist "test_docs\Scripts\activate.bat" (
    echo ERROR: Virtual environment 'test_docs' not found
    echo Please run 'setup_test.bat' first to create the environment
    exit /b 1
)

REM Recreate output directory to force a full rebuild
if exist "test_docs_results" (
    echo Removing existing output directory: test_docs_results
    rmdir /s /q test_docs_results
)
echo Creating output directory: test_docs_results
mkdir test_docs_results

echo Activating virtual environment...
call test_docs\Scripts\activate.bat

echo.
echo Building HTML documentation...
echo Source: docs
echo Output: test_docs_results
echo.

REM Run Sphinx build using the virtual environment's Python
test_docs\Scripts\python.exe -m sphinx -b html -E -a docs test_docs_results
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Sphinx build failed
    call test_docs\Scripts\deactivate.bat 2>nul
    exit /b 1
)

echo.
echo ====================================
echo Build Complete!
echo ====================================
echo.
echo Documentation generated in: test_docs_results
echo.
echo On Windows platform, the output will likely show a number (approx 600 warnings).
echo This is not a problem. The purpose of this script is to generate the HTML documentation on a Windows platform,
echo without the need to build the container.
echo The Sphinx documentation referenced Python package documentation being generated with pdoc.
echo These are not available in the local test environment. Ignore these warnings.
echo The HTML documentation should still be generated.
echo.
echo To view the documentation:
echo   1. Open: test_docs_results\index.html
echo   2. Or run: start test_docs_results\index.html
echo.

REM Deactivate virtual environment
call test_docs\Scripts\deactivate.bat 2>nul

exit /b 0
