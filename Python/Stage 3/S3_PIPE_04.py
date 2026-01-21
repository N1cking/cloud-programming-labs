def to_floats(values):
    for item in values:
        try:
            yield float(item.strip())
        except (ValueError, AttributeError):
            continue


values = [" 1 ", "x", "2.5", " -3 ", "junk"]

numbers = to_floats(values)
doubled = (n * 2 for n in numbers)
result = sum(doubled)

print(result)
