def validate_float(value):
    try:
        float_value = float(value)
        return float_value
    except ValueError:
        return None

def validate_choice(value, choices):
    if value in choices:
        return value
    else:
        return None
