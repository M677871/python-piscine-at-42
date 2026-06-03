*This project has been created as part of the 42 curriculum by miissa.*

# The Matrix - Welcome to the Real World of Data Engineering

## Description

The Matrix is a Python project focused on learning the foundational tools used in modern data engineering workflows.

Through a Matrix-themed journey, you will discover how to create isolated Python environments, manage project dependencies, and securely configure applications using environment variables.

Focus areas:

* Virtual environments (`venv`)
* Dependency management (`pip` & Poetry)
* Environment variables and configuration management
* Reproducible development environments
* Secure handling of application secrets

---

## Exercises

| Part                                 | Files  | Topic                                                         |
| ------------------------------------ | ------ | ------------------------------------------------------------- |
| Exercise 0 – Entering the Matrix     | `ex0/` | Virtual environments, Python environment inspection           |
| Exercise 1 – Loading Programs        | `ex1/` | Package management, pip vs Poetry, data analysis              |
| Exercise 2 – Accessing the Mainframe | `ex2/` | Environment variables, `.env` files, configuration management |

---

## Project Structure

```text
├── ex0
│   └── construct.py
├── ex1
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
├── ex2
│   ├── oracle.py
│   ├── .env.example
│   └── .gitignore
└── README.md
```

Each exercise introduces a real-world tool commonly used by data engineers and software developers.

---

## Usage

### Exercise 0

```bash
python3 construct.py
```

Create and activate a virtual environment:

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py
```

### Exercise 1

Using pip:

```bash
pip install -r requirements.txt
python3 loading.py
```

Using Poetry:

```bash
poetry install
poetry run python3 loading.py
```

### Exercise 2

Create a configuration file:

```bash
cp .env.example .env
```

Run the program:

```bash
python3 oracle.py
```

Override configuration with environment variables:

```bash
MATRIX_MODE=production python3 oracle.py
```

---

## Key Concepts

* Python virtual environments (`venv`)
* Environment isolation
* Dependency management
* pip and requirements files
* Poetry package management
* Data analysis with NumPy and Pandas
* Data visualization with Matplotlib
* Environment variables
* Configuration management
* Secure handling of secrets
* Development vs production environments

---

## Resources

* Python Documentation
* Poetry Documentation
* NumPy Documentation
* Pandas Documentation
* Matplotlib Documentation
* ChatGPT
* Google Gemini

---

## AI Assistance

* AI was used for explanations, troubleshooting, and documentation support.
* All submitted code was reviewed, understood, and tested by me.
* AI assistance was used in accordance with the project's guidelines.
