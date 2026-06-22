# Advanced Playwright Python Framework

This is a scalable Playwright automation framework for e-commerce UI testing using Python and Pytest.

## Features

- Page Object Model
- JSON-based test data
- Environment configuration
- Browser selection from command line
- HTML reporting
- Allure reporting
- Screenshot capture on failure
- Logging
- Smoke and regression markers
- Parallel execution ready

## Application Under Test

- https://www.saucedemo.com/

## Installation

```bash
pip install -r requirements.txt
python -m playwright install
```

## Run Tests

### Run all tests
```bash
pytest
```

### Run on firefox
```bash
pytest --browser=firefox
```

### Run on qa environment
```bash
pytest --env=qa
```

### Run smoke tests
```bash
pytest -m smoke
```

### Run regression tests
```bash
pytest -m regression
```

### Parallel execution
```bash
pytest -n 2
```

## Reports

### HTML report
```text
reports/report.html
```

### Allure results
To generate Allure results:
```bash
pytest --alluredir=allure-results
```

Then serve report:
```bash
allure serve allure-results
```

## Screenshots

Failure screenshots are stored in:
```text
screenshots/
```