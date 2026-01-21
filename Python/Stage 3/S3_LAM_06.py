def map_values(d, fn):
    return {k: fn(v) for k, v in d.items()}


print(map_values({"a": 1, "b": 2}, lambda v: v * 10))
