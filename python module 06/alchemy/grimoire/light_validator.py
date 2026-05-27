def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    low_ing = ingredients.lower()
    is_valid = any(a in low_ing for a in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients}- {status}"
