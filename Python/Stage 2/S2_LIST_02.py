def unique(values):
    result = []
    for item in values:
        if item not in result:
            result.append(item)
    return result


print(unique([1, 2, 1, 3, 2, 4]))
print(unique(["a", "b", "a", "c"]))
