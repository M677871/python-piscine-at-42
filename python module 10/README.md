*This project has been created as part of the 42 curriculum by miissa.*

# FuncMage Chronicles – Mastering the Ancient Arts of Functional Programming

## Description

FuncMage Chronicles is a Python module dedicated to exploring the principles of functional programming. Set in a futuristic fantasy world, the project introduces powerful concepts such as lambda expressions, higher-order functions, closures, decorators, and the tools provided by Python's `functools` module.

Through five progressive exercises, you will learn how functions can be treated as first-class objects, how closures preserve state without global variables, and how decorators can extend behavior while keeping business logic clean and reusable.

By the end of the module, you will have a practical understanding of functional programming patterns and how they can be applied to write elegant, maintainable Python code.

---

## Exercises

| Exercise                     | Files                    | Topic                                                                      |
| ---------------------------- | ------------------------ | -------------------------------------------------------------------------- |
| Exercise 0 – Lambda Sanctum  | `lambda_spells.py`       | Lambda expressions, `map`, `filter`, `sorted`, functional transformations  |
| Exercise 1 – Higher Realm    | `higher_magic.py`        | Higher-order functions, function composition, first-class functions        |
| Exercise 2 – Memory Depths   | `scope_mysteries.py`     | Closures, lexical scoping, persistent state, `nonlocal`                    |
| Exercise 3 – Ancient Library | `functools_artifacts.py` | `reduce`, `partial`, `lru_cache`, `singledispatch`                         |
| Exercise 4 – Master's Tower  | `decorator_mastery.py`   | Decorators, parameterized decorators, retries, validation, `@staticmethod` |

---

## Project Structure

At the end of the module, your repository should resemble:

```text
.
├── ex0
│   └── lambda_spells.py
├── ex1
│   └── higher_magic.py
├── ex2
│   └── scope_mysteries.py
├── ex3
│   └── functools_artifacts.py
└── ex4
    └── decorator_mastery.py
```

Each exercise is independent and focuses on a specific functional programming concept.

---

## Usage

Make sure Python 3.10+ is installed, then execute the exercises individually:

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

To verify coding standards:

```bash
flake8 .
```

---

## Key Concepts Covered

### Functional Programming Fundamentals

* First-class functions
* Function composition
* Higher-order functions
* Immutable-style programming patterns

### Lambda Expressions

* Anonymous functions
* Collection transformations
* Sorting, filtering, and mapping

### Closures and Lexical Scoping

* Capturing variables from outer scopes
* Persistent state without global variables
* `nonlocal` usage

### Functools Utilities

* `functools.reduce`
* `functools.partial`
* `functools.lru_cache`
* `functools.singledispatch`

### Decorators

* Function wrappers
* Parameterized decorators
* Retry mechanisms
* Execution timing
* Validation logic

### Static Methods

* Class utilities independent from object state
* Differences between instance methods and static methods

---

## Concepts Demonstrated

### Higher-Order Functions

Functions can be passed as arguments and returned from other functions.

Example use cases:

* Spell amplification
* Conditional spell casting
* Spell combinations
* Spell sequences

### Closures

Functions retain access to variables from their creation environment.

Example use cases:

* Independent counters
* Power accumulators
* Memory vaults
* Factory-generated enchantments

### Memoization

Caching expensive computations using `lru_cache`.

Benefits:

* Reduced recursion overhead
* Improved performance
* Reuse of previously computed results

### Decorator-Based Design

Separates concerns such as:

* Timing
* Validation
* Error handling
* Retry logic

from the core business logic.

---

## Resources

1. Python official documentation: https://docs.python.org/3/
2. Functional Programming HOWTO: https://docs.python.org/3/howto/functional.html
3. functools documentation: https://docs.python.org/3/library/functools.html
4. collections.abc documentation: https://docs.python.org/3/library/collections.abc.html
5. Flake8 documentation: https://flake8.pycqa.org/

---

## AI Assistance

1. AI was used to clarify functional programming concepts, closures, decorators, and `functools` utilities.
2. All code submitted is fully written, tested, and understood by me.
3. AI helped improve explanations, documentation structure, and README formatting.
