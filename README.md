# Playwright UI Automation

Automated UI testing project using Playwright and Pytest.

## Technology Stack

* Python 3.12+
* Playwright
* Pytest
* Pytest HTML Reporter

## Project Structure

```text
playwright-ui-automation/
│
├── pages/
│   ├── __init__.py
│   └── home_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_demo_webshop.py
│
├── reports/
│
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Scenario

Website:
https://demowebshop.tricentis.com/

### Scenario: Product Search

1. Open Demo Web Shop website
2. Input product keyword
3. Click Search button
4. Verify search result is displayed

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/playwright-ui-automation.git
cd playwright-ui-automation
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows

```bash
venv\Scripts\activate
```

Linux / MacOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests with browser visible:

```bash
pytest --headed
```

Run specific test file:

```bash
pytest tests/test_demo_webshop.py
```

## Test Report

Generate HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Generated report:

```text
reports/
└── report.html
```

Open the report in browser:

```bash
start reports/report.html
```

## Sample Test Result

| Test Case      | Result |
| -------------- | ------ |
| Search Product | PASS   |
