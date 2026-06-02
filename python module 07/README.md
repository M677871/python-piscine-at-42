*This project has been created as part of the 42 curriculum by miissa.*

# DataDeck - Abstract Card Architecture

## Description

DataDeck is a Python module focused on mastering object-oriented design patterns via a creature-based battle system.

You will build a modular architecture inspired by collectible card games: creatures are dynamically created, gain special abilities, and battle in tournaments.

Focus areas:
- Abstract Factory Pattern (creature creation)
- Capability-based design (healing & transformation)
- Strategy Pattern (battle behavior)

---

## Exercises

| Part | Files | Topic |
|------|------|------|
| Part I – Creature Forge | `ex0/` | Abstract Factory, base/evolved creatures |
| Part II – Arcane Capabilities | `ex1/` | Capability system, healing & transform mixins |
| Part III – Tournament Engine | `ex2/` | Strategy Pattern, battle orchestration |

---

## Project Structure
├── ex0
│ ├── init.py
│ ├── creature.py
├── ex1
│ ├── init.py
│ ├── capabilities.py
├── ex2
│ ├── init.py
│ ├── strategies.py
├── battle.py
├── capacitor.py
├── tournament.py
└── README.md


All classes and methods are intentionally simple and return strings or basic outputs. The focus is architecture, not game complexity.

---

## Usage

```bash
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

## Key Concepts
- Abstract classes & interfaces (ABC, abstractmethod)
- Abstract Factory Pattern
- Multiple inheritance for capabilities
- Composition vs inheritance
- Strategy Pattern
- Runtime validation & polymorphism
- Separation of concerns

## Resources
- Python docs
- ChatGPT, google gemini

## AI Assistance
- AI clarified design patterns and architecture
- All code fully written and understood by me
- AI improved README clarity and formatting