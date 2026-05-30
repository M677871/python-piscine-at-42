*This project has been created as part of the 42 curriculum by miissa.*

# The Codex - Mastering Python’s Import Mysteries

## Description

The Codex is a Python module focused on mastering the dark art of imports. Through an alchemical narrative, this project explores Python’s package system, module resolution, absolute vs relative imports, and the dangers of circular dependencies.

Across four progressive stages, you will build a complete “alchemist laboratory” package and learn how Python transforms folders into modules, resolves import paths, and executes code in complex dependency graphs.

By the end, you will have a deep understanding of Python’s import mechanics, not just how to use them, but how they behave internally.

---

## Exercises

| Part | Files | Topic |
|------|------|------|
| Part I – The Alembic | `ft_alembic_0.py → ft_alembic_5.py`, `elements.py`, `alchemy/` | Package initialization, basic imports, module exposure, `__init__.py` behavior |
| Part II – Distillation | `ft_distillation_0.py → ft_distillation_1.py`, `alchemy/potions.py` | Nested imports, module aliasing, package API design |
| Part III – The Great Transmutation | `ft_transmutation_0.py → ft_transmutation_2.py`, `alchemy/transmutation/` | Absolute vs relative imports, module resolution strategies |
| Part IV – Avoid the Explosion | `ft_kaboom_0.py → ft_kaboom_1.py`, `alchemy/grimoire/` | Circular dependencies and import failure patterns |

---

## Project Structure

At the end of the module, your repository should resemble:

```
.
├── alchemy
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── grimoire
│   │   ├── __init__.py
│   │   ├── light_spellbook.py
│   │   ├── light_validator.py
│   │   ├── dark_spellbook.py
│   │   └── dark_validator.py
│   └── transmutation
│       ├── __init__.py
│       └── recipes.py
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_alembic_2.py
├── ft_alembic_3.py
├── ft_alembic_4.py
├── ft_alembic_5.py
├── ft_distillation_0.py
├── ft_distillation_1.py
├── ft_transmutation_0.py
├── ft_transmutation_1.py
├── ft_transmutation_2.py
├── ft_kaboom_0.py
└── ft_kaboom_1.py
```

All functions in this project are intentionally simple and return strings or basic structures. The focus is on import behavior, not algorithmic complexity.

---

## Usage

Make sure Python 3.10+ is installed, then run any script from the repository root:

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py
python3 ft_alembic_5.py

python3 ft_distillation_0.py
python3 ft_distillation_1.py

python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py

python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
```

---

## Key Concepts Covered

- Python package initialization (`__init__.py`)
- Import styles: `import x` vs `from x import y`
- Absolute imports vs relative imports
- Module exposure and API design
- Nested imports across packages
- Circular dependency detection and failure modes
- Python import system internals

---

## Resources

1. Python official documentation: https://docs.python.org/3/
2. Modules and packages: https://docs.python.org/3/tutorial/modules.html
3. Import system reference: https://docs.python.org/3/reference/import.html
4. `typing` module: https://docs.python.org/3/library/typing.html
5. Flake8 documentation: https://flake8.pycqa.org/

---

## AI Assistance

1. AI was used to clarify Python import mechanics and module structure rules.
2. All code submitted is fully written and understood by me.
3. AI helped improve clarity, consistency, and formatting of this README.
```