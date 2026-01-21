def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}


defaults = {"host": "localhost", "port": 5432, "options": {"ssl": False}}
overrides = {"port": 6543, "options": {"ssl": True}}

merged = merge_defaults(defaults, overrides)
print(merged)
# Shallow merge: nested dicts are replaced, not deep-merged.
