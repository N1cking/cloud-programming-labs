def omit(d, keys):
    key_set = set(keys)
    return {k: v for k, v in d.items() if k not in key_set}


print(omit({"a": 1, "b": 2, "c": 3}, ["b", "x"]))
