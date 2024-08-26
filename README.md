# QA-Automation-Assessment
Technical Assessment for ScanSource

## Overview
This project is a technical assessment for ScanSource, using Python's Pytest framework and Selenium for automated testing.

### Key Features
1. **Testing Framework:** Utilizes Pytest and Selenium for test automation.
2. **Code Validation:** Employs `ruff` for code linting and validation.
3. **Report Generation:** Generates reports using `pytest-html-reporter`.
4. **Test Dependencies:** Implements test dependencies using `pytest-dependency`.
5. **WebDriver Management:** Uses `webdriver-manager` to download and launch WebDriver automatically.


## Installation

To get started, switch to the root directory of the project and install the required dependencies:
```bash
$ pip install -r requirements.txt
```

## Structure of the framework 

1. **Pages:** Contains the page objects that define the structure and behavior of the web pages.
2. **Setting:** Includes WebDriver configuration and other necessary settings.
3. **Tests:** Contains all test cases. 
4. **Configuration:** `Pytest.ini` and `conftest.py`  for Pytest configuration.
5. `pyproject.toml` for Ruff configuration.
6. **Reports:** The HTML_Report folder contains the generated test reports.

## Running Tests

1. To run the tests, you can either open the project in PyCharm and execute the tests directly from the IDE or run specific tests using the command line.