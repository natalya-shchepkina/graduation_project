# Graduation project

The project consists of two parts - API tests for a hotel website and UI tests for Demoblaze.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Tests](#running-the-tests)

## Introduction

The Website Hotel API tests cover different scenarios and verify the expected behavior of the API responses.
The Demoblaze Selenium UI tests ensure the correctness and reliability of pages. These tests cover different scenarios and verify the expected behavior of the product forms, registration of user, adding and removing products.


## Prerequisites

Before running the tests, make sure you have the following prerequisites:

- Python 3.x installed on your system
- `pip` package manager installed

## Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/natalya-shchepkina/graduation_project.git
   ```

2. Navigate to the project directory:

   ```shell
   cd graduation_project
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate.bat
     ```

   - For Unix or Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```


## Running the Tests

To run the API tests, use the following command:

```shell
python -m pytest .\tests
```

This command will execute all the tests and display the test results in the console.
All information for reporting will be collected in the `allure-results`.

To run the tests with the `pytest_addoption` function options, you can follow these instructions:

Run the tests using the `pytest` command and specify the options:

   ```shell
   pytest --browser chrome --url http://127.0.0.1:8081 
   ```

   Replace the following options with your desired values:
   - `--browser`: Specify the browser to run the tests (e.g., `chrome`, `firefox`).
   - `--url`: Specify the base URL.
   - `--headless`: Specify to run UI tests without displaying the interface.
   - `--log_level`: Specify the logging level
   - `--local`: Specify to run tests locally
   - `--executor`: Specify to run tests remotely
   - `--selenoid_vnc`: Specify for browser display
   - `--selenoid_log`: Specify to logging
   - `--browser_version`: Specify browser version

