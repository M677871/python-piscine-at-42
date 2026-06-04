*This project has been created as part of the 42 curriculum by miissa.*

# Cosmic Data – Discover Pydantic Models & Validation

## Description

Cosmic Data is a Python project designed to introduce and reinforce the fundamentals of data validation using **Pydantic 2.x**.

Through a space-themed journey, you will learn how to create robust data models, enforce validation rules, handle nested structures, and build reliable data-processing systems.

The project progresses from simple field validation to advanced business logic and nested model relationships.

Focus areas:

* Pydantic `BaseModel`
* Field validation with `Field`
* Type annotations and static analysis
* Custom validation using `@model_validator`
* Enums and constrained values
* Nested models
* Data integrity and error handling
* Automatic type conversion
* Validation error reporting

---

## Exercises

| Part                               | Files  | Topic                                         |
| ---------------------------------- | ------ | --------------------------------------------- |
| Exercise 0 – Space Station Data    | `ex0/` | Basic Pydantic models and field validation    |
| Exercise 1 – Alien Contact Logs    | `ex1/` | Custom business rules with `@model_validator` |
| Exercise 2 – Space Crew Management | `ex2/` | Nested models and complex validation logic    |

---

## Project Structure

```text
├── ex0
│   └── space_station.py
├── ex1
│   └── alien_contact.py
├── ex2
│   └── space_crew.py
└── README.md
```

Each exercise introduces a new Pydantic concept while building upon knowledge gained from previous exercises.

---

## Requirements

* Python 3.10+
* Pydantic 2.x
* flake8
* mypy

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install pydantic
```

Verify the installed version:

```bash
python -c "import pydantic; print(pydantic.__version__)"
```

---

## Usage

### Exercise 0

```bash
cd ex0
python3 space_station.py
```

Demonstrates:

* Basic Pydantic model creation
* Field constraints
* Datetime handling
* Validation errors

---

### Exercise 1

```bash
cd ex1
python3 alien_contact.py
```

Demonstrates:

* Enum usage
* Custom validation rules
* Business logic validation
* Model-wide validation with `@model_validator`

---

### Exercise 2

```bash
cd ex2
python3 space_crew.py
```

Demonstrates:

* Nested Pydantic models
* Lists of validated objects
* Mission safety requirements
* Complex validation across multiple fields

---

## Validation Checks

Run flake8:

```bash
flake8 .
```

Run mypy:

```bash
mypy .
```

Run all exercises:

```bash
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py
```

---

## Key Concepts

### BaseModel

The foundation of every Pydantic model.

```python
class CrewMember(BaseModel):
    ...
```

Provides automatic validation and type conversion.

---

### Field Validation

Use `Field()` to enforce constraints.

```python
age: int = Field(..., ge=18, le=80)
```

Ensures values remain within an accepted range.

---

### Enum Types

Restrict values to predefined choices.

```python
class Rank(str, Enum):
    commander = "commander"
```

Prevents invalid input values.

---

### model_validator

Validate relationships between fields.

```python
@model_validator(mode="after")
def validate_mission(self):
    ...
```

Useful for business rules that depend on multiple fields.

---

### Nested Models

Models can contain other models.

```python
crew: list[CrewMember]
```

Pydantic automatically validates every nested object.

---

### Automatic Type Conversion

Pydantic can convert compatible values automatically.

Example:

```python
launch_date="2024-07-01T08:00:00"
```

becomes:

```python
datetime(...)
```

during validation.

---

## Learning Outcomes

After completing this project, you should be able to:

* Create validated data models with Pydantic
* Define field constraints
* Build custom validation logic
* Use enums effectively
* Handle nested data structures
* Understand automatic type conversion
* Interpret validation errors
* Write type-safe Python code
* Pass static analysis using mypy
* Follow flake8 coding standards

---

## Resources

* Pydantic Documentation
* Python Documentation
* mypy Documentation
* flake8 Documentation
* ChatGPT
* Google Gemini

---

## AI Assistance

* AI was used for explanations, troubleshooting, and documentation support.
* All submitted code was reviewed, understood, and tested by me.
* AI assistance was used in accordance with the project's guidelines.
