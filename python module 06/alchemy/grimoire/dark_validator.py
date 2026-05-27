from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    low_ing = ingredients.lower()
    is_valid = any(a in low_ing for a in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients}- {status}"
