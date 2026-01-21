def get_path(obj, path, fallback=None):
    current = obj
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return fallback
        current = current[part]
    return current


sample = {"a": {"b": {"c": 42}}}
print(get_path(sample, "a.b.c", "missing"))
print(get_path(sample, "a.b.x", "missing"))
print(get_path(sample, "a.b", "missing"))
