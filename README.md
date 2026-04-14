# Ebay Prices UI Automation Tests

This project contains automated UI tests for the eBay web application using **Selenium + Pytest + Allure**.

---

## 🔧 Setup (Manual)

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run Tests (Recommended - One Command)

### 🪟 Windows

```powershell
.\run_tests.bat
```

### 🍎 Mac

```bash
bash run_tests.sh
```

👉 This will:

* create/activate virtual environment
* install dependencies
* run tests
* open Allure report (if installed)

---

## 📊 Allure Report (Optional)

If Allure is installed, the report will open automatically.

If not installed, tests will still run and results will be saved in:

```
allure-results/
```

### Install Allure:

**Mac:**

```bash
brew install allure
```

**Windows:**

```bash
scoop install allure
```

Or download manually:
https://github.com/allure-framework/allure2/releases

---

## 🧪 Run Tests Manually

```bash
pytest e2e_tests/tests/ --log-cli-level=INFO -v
```

---

## 🔁 Run Tests Multiple Times

Using `pytest-repeat`:

```bash
pytest e2e_tests/tests/test_prices.py --count=20 -v
```

---

## 📁 Project Structure

```
.
├── e2e_tests/
├── run_tests.bat
├── run_tests.sh
├── requirements.txt
└── README.md
```

---

## 💡 Notes

* Logging is enabled for debugging test flow
* Screenshots are automatically attached to Allure on failure
* Scripts support both Windows and Mac environments
