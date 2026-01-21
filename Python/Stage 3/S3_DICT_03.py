def pick(d, keys):
    return {k: d[k] for k in keys if k in d}


print(pick({"a": 1, "b": 2, "c": 3}, ["a", "c", "x"]))
