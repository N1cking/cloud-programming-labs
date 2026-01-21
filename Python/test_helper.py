def eq(actual, expected):
    if actual != expected:
        raise ValueError(f"Expected {expected}, but got {actual}")