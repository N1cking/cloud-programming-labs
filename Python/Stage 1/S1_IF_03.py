def normalize_name(x):
    if not x:
        return "Anonymous"

    trimmed = x.strip()
    if not trimmed:
        return "Anonymous"

    return trimmed


print(normalize_name(""))
print(normalize_name(" "))
print(normalize_name(None))
print(normalize_name(" Ola "))
