def pipe(*fns):
    def apply(value):
        result = value
        for fn in fns:
            result = fn(result)
        return result

    return apply


def collapse_spaces(text):
    return " ".join(text.split())


normalize = pipe(str.strip, str.lower, collapse_spaces)
print(normalize(" Ala Ma Kota "))
