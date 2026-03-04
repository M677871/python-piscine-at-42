*This project has been created as part of the 42 curriculum by miissa.*

# Code Nexus - OOP, Abstract Classes & Pipelines

## Description

Code Nexus is the fifth Python module of the 42 piscine. It focuses on
object-oriented programming with abstract base classes, polymorphism,
protocols, and composable pipeline architectures. Each exercise builds toward
a full enterprise-style stream processing system, reinforcing clean design
patterns and the use of Python's `abc`, `typing`, and `collections` modules.

## Exercises

| Exercise | File | Topic |
|----------|------|-------|
| ex0 | `stream_processor.py` | Abstract base class, polymorphism (Numeric / Text / Log processors) |
| ex1 | `data_stream.py` | Inheritance, specialised stream types (Sensor / Transaction / Event) |
| ex2 | `nexus_pipeline.py` | Protocols, pipeline stages, adapters and a top-level `NexusManager` |

## Usage

Make sure Python 3.10+ is installed, then run any exercise from the
module root:

```bash
py ex0/stream_processor.py
py ex1/data_stream.py
py ex2/nexus_pipeline.py
```

## Resources

1. Python official documentation: https://docs.python.org/3/
2. `abc` module reference: https://docs.python.org/3/library/abc.html
3. `typing` module reference: https://docs.python.org/3/library/typing.html
4. GeeksforGeeks Python tutorials: https://www.geeksforgeeks.org/

## AI Assistance

1. AI was used to clarify Python syntax and to fix flake8 violations.
2. All code submitted is fully written and understood by me.
3. AI helped improve the readability and clarity of this README.