#!/bin/bash

echo "Activating virtual environment..."

# Create venv if not exists
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

echo ""
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Checking if Allure is installed..."

if ! command -v allure &> /dev/null
then
    echo "❌ Allure is NOT installed."
    echo ""
    echo "To install Allure:"
    echo "Run: brew install allure"
    echo "Or download from:"
    echo "https://github.com/allure-framework/allure2/releases"
    echo ""
    echo "Running tests WITHOUT opening Allure report..."

    pytest --alluredir=allure-results

    echo ""
    echo "✅ Tests finished. Results saved in 'allure-results' folder."
    exit 0
fi

echo "✅ Allure is installed!"

echo ""
echo "Running tests..."
pytest --alluredir=allure-results

echo ""
echo "Opening Allure report..."
allure serve allure-results