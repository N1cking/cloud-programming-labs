def invert(d):
    result = {}
    for key, value in d.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result


print(invert({"a": 1, "b": 2, "c": 1}))
