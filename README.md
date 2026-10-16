# Playwright CI/CD Regression Automation Suite

A production-ready, ultra-fast End-to-End (E2E) automated regression testing suite designed for **SauceDemo** web application. This project uses **Python Playwright** and is fully integrated with **GitHub Actions** for continuous integration (CI) pipelines.

---

## Tech Stack & Prerequisites

- **Language:** Python 3.10+
- **Automation Framework:** Playwright (Synchronous API)
- **CI/CD Platform:** GitHub Actions
- **Target Application:** [SauceDemo](https://www.saucedemo.com/)

---

## Project Architecture

```text
.
├── .github/
│   └── workflows/
│       └── playwright.yml    # CI/CD Pipeline Configuration
├── sauce_test.py             # E2E Core Automation Script
└── requirements.txt          # Python Dependencies List
```

---

## Local Setup & Execution

Follow these precise steps to configure and execute the test suite on your local workstation:

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-folder-name>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Run the Automation Script (Headed Mode)
To visually observe the browser interaction locally:
*Open `sauce_test.py` and ensure `headless=False` is set during development.*
```bash
python sauce_test.py
```

---

## CI/CD Integration (GitHub Actions)

This project features a fully automated **DevOps Pipeline** that executes the regression suite automatically on cloud architecture (`ubuntu-latest`) whenever a developer triggers:
- A code `push` to `main` or `master` branches.
- A `pull_request` targetted at `main` or `master` branches.

### Pipeline Highlights:
- **Headless Mode Compulsory:** Overridden to `headless=True` for efficient, non-GUI virtual display execution on GitHub servers.
- **Auto-Dependency Installation:** Resolves system dependencies and Linux packages instantly via `--with-deps`.

---

## Automated Test Coverage Scenarios

| Scenario ID | Component | Description | Test Type | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **TC_001** | Authentication | Successful user login with valid credentials. | Positive | High |
| **TC_002** | Catalog | Adding a core retail item to the shopping cart. | Positive | High |
| **TC_003** | Checkout Navigation | Validating smooth transition to the checkout process. | Positive | High |

---

## QA Contact Information
- **Maintained By:** Ram, QA Automation Engineer
- **Role:** Manual/Automation-Hybrid QA Professional
- **Framework Status:** Active / Production Ready
