from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    lower_case_ingredients: str = ingredients.lower()
    is_valid: bool = any(a in lower_case_ingredients for a in allowed)
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients}- {status}"
