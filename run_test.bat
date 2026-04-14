@echo off

echo Activating virtual environment...
call .venv\Scripts\activate

echo.
echo Checking if Allure is installed...

where allure >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Allure is NOT installed.
    echo.
    echo To install Allure:
    echo 1. Download from:
    echo    https://github.com/allure-framework/allure2/releases
    echo 2. Extract and add "bin" folder to PATH
    echo OR use:
    echo    scoop install allure
    echo.
    echo Running tests WITHOUT opening Allure report...
    pytest --alluredir=allure-results
    echo.
    echo ✅ Tests finished. Results saved in "allure-results" folder.
    exit /b 0
)

echo ✅ Allure is installed!

echo.
echo Running tests...
pytest --alluredir=allure-results

echo.
echo Opening Allure report...
allure serve allure-results