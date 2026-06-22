# QA Automation Portfolio

This repository showcases a hybrid automation testing portfolio for web UI and API validation.

## Tech Stack

- **Selenium + Java**
- **Playwright + Python**
- **API Testing with Python Requests**
- **TestNG**
- **Pytest**
- **GitHub Actions**

## Project Structure

```text
qa-automation-portfolio/
├── README.md
├── selenium-java-framework/
├── playwright-python-framework/
├── api-testing/
└── .github/workflows/
```

## Modules

### 1. Selenium Java Framework
Features:
- Page Object Model
- TestNG execution
- Reusable base setup
- Sample login test

### 2. Playwright Python Framework
Features:
- Modern UI automation
- Page classes
- Pytest execution
- Headless/headed support

### 3. API Testing Framework
Features:
- REST API test coverage
- Status code validation
- Response assertions
- Reusable API utilities

## How to Run

### Selenium Java
```bash
cd selenium-java-framework
mvn clean test
```

### Playwright Python
```bash
cd playwright-python-framework
pip install -r requirements.txt
playwright install
pytest
```

### API Testing
```bash
cd api-testing
pip install -r requirements.txt
pytest
```

## Portfolio Highlights

- UI automation using two popular frameworks
- API automation with assertions
- Clean project organization
- Beginner-friendly and recruiter-friendly structure
- Ready for future CI/CD improvements

## Future Enhancements

- Reporting with Allure or Extent Reports
- Data-driven testing
- Environment configuration
- Jenkins/GitHub Actions advanced pipelines
- Cross-browser execution
