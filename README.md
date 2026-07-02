# OrangeHRM Playwright Python Automation Framework

## 📌 About the Project

This is a beginner-friendly UI automation framework developed using **Playwright with Python** and **Pytest**. The project automates common user scenarios in the OrangeHRM demo application and follows the **Page Object Model (POM)** design pattern to keep the test code organized and easy to maintain.

The purpose of this project is to practice Playwright automation, build a reusable test framework, and demonstrate automation testing skills through Github.

---

## 🛠️ Technologies Used

* Python
* Playwright
* Pytest
* Pytest-HTML
* Git & GitHub
* GitHub Actions (CI/CD)

---

## 📂 Project Structure

```text
orangehrm-playwright/
│
├── pages/               # Page Object classes
├── tests/               # Test cases
├── reports/             # HTML test reports
├── screenshots/         # Failed test screenshots
├── config.py            # Application URL and test data
├── conftest.py          # Pytest fixtures
├── requirements.txt     # Project dependencies
├── .github/workflows/   # GitHub Actions workflow
└── README.md
```

---

## ✨ Features

* Page Object Model (POM)
* Reusable test framework
* Smoke and Regression test execution
* HTML test reporting
* Automatic screenshots for failed test cases
* Continuous Integration using GitHub Actions

---

## 📥 Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/AswathyJoshin/orangehrm-playwright-python-framework.git
```

Move into the project folder.

```bash
cd orangehrm-playwright-python-framework
```

---

## ⚙️ Install Dependencies

Create and activate a virtual environment (recommended).

Install the required packages.

```bash
pip install -r requirements.txt
```

Install Playwright browsers.

```bash
playwright install
```

---

## ▶️ Running the Tests

Run all test cases.

```bash
pytest -v
```

Run only smoke tests.

```bash
pytest -m smoke -v
```

Generate an HTML report.

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## 📊 Test Reporting

After execution:

* HTML reports are generated inside the **reports** folder.
* If a test fails, a screenshot is automatically saved inside the **screenshots** folder to help with debugging.

---

## 🔄 Continuous Integration (CI/CD)

This project uses **GitHub Actions** to automate test execution.

Whenever code is pushed to the repository or a pull request is created:

* Dependencies are installed automatically.
* Playwright browsers are installed.
* Test cases are executed.
* The workflow status is displayed in the **Actions** tab of the GitHub repository.

---

## 🧪 Test Scenarios Covered

* Valid Login
* Invalid Username
* Invalid Password
* Empty Username
* Empty Password
* Login Page UI Validation
* Logout
* Session Security

---

## 👨‍💻 Author

**Aswathy George Kuzhivelipurath**

GitHub: https://github.com/AswathyJoshin

Linkedln: https://www.linkedin.com/in/aswathy-george-k/

---

## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes only.

It uses the publicly available OrangeHRM demo application to demonstrate UI automation using Playwright and Pytest.

This project is not affiliated with, endorsed by, or sponsored by OrangeHRM. All trademarks, product names, and logos are the property of their respective owners.

---

## 🤝 Acknowledgements

Special thanks to the OrangeHRM team for providing a publicly accessible demo application that allows learners and QA engineers to practice UI automation and testing techniques.
