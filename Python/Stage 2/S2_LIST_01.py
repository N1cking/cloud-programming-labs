def clean_numbers(values):
    cleaned = []
    for item in values:
        try:
            cleaned.append(float(item.strip()))
        except (ValueError, AttributeError):
            continue
    return cleaned


print(clean_numbers([" 1 ", "x", "2"]))
print(clean_numbers(["3.5", " -2 ", "", "7"]))
