# SauceDemo Automation Framework (Selenium + Pytest + POM)

This repository contains an automation testing framework for [SauceDemo](https://www.saucedemo.com/)  
using **Selenium, Pytest, and the Page Object Model (POM).**

---

## 📂 Project Structure
saucedemo-automation/
│── .gitignore
│── README.md
│── requirements.txt
│── pytest.ini
│── conftest.py
│
├── pages/
│   │── __init__.py
│   │── login_page.py
│   │── home_page.py
│   │── cart_page.py
│   │── checkout_page.py
│
├── tests/
│   │── __init__.py
│   │── test_login.py
│   │── test_cart.py
│   │── test_checkout.py
│
└── reports/        # auto-generated after pytest run

