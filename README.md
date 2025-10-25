# BISB CI/CD Project

## Objective
Automate the testing and continuous integration process for the **BISB (Business Intelligence for Beauty Salons)** system, ensuring code quality and reliability before deployment.

---

## Project Overview
This repository implements the first stage of a DevOps pipeline: Continuous Integration (CI) using GitHub Actions and Pytest.  
Each code update pushed to the `develop` branch automatically triggers the test suite.  
Pull requests to the `main` branch must successfully pass all tests before being merged into production.

---

## Steps Implemented
1. Repository creation and branch strategy (`develop` and `main`).
2. Unit test implementation using Pytest.
3. CI workflow setup with GitHub Actions.
4. Documentation and preparation for the Continuous Deployment (CD) phase.

---

## Local Testing
To run tests locally:

```bash
pip install -r requirements.txt
pytest -v
