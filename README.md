# Pytest Python Selenium Framework

A robust and scalable automation testing framework built with **Python**, **Selenium**, and **Pytest**, integrated with **GitHub Actions** for Continuous Integration/Continuous Deployment (CI/CD). This framework is designed to streamline the testing process for web applications, ensuring high-quality software delivery.


## Project Overview

This automation framework leverages **Selenium WebDriver** for browser automation and **Pytest** for test execution and reporting. Integrated with **GitHub Actions**, it ensures that tests are automatically run on each commit, facilitating continuous quality assurance.

## Features

- **Cross-Browser Testing:** Supports multiple browsers like Chrome, Firefox, and Edge.
- **Parallel Test Execution:** Reduces test execution time by running tests concurrently.
- **Data-Driven Testing:** Utilizes external data sources (CSV, JSON) for test inputs.
- **Page Object Model (POM):** Enhances maintainability and readability by separating page elements and actions.
- **CI/CD Integration:** Automates test runs on GitHub Actions with each commit or pull request.
- **Detailed Reporting:** Generates comprehensive HTML reports with screenshots on test failures.
- **Reusable Utilities:** Includes helper functions for common tasks like logging, configuration management, and more.

## Technologies Used

- **Programming Language:** Python 3.x
- **Automation Tool:** Selenium WebDriver
- **Testing Framework:** Pytest
- **Dependency Management:** Poetry
- **Continuous Integration:** GitHub Actions
- **Reporting:** Pytest HTML Report
- **Version Control:** Git & GitHub

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+** installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).
- **Git** installed for version control. Download it from [Git's official website](https://git-scm.com/downloads).
- **Poetry** for dependency management. Install it using the following command:
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
