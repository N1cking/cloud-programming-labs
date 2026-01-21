def is_truthy(v):
    return bool(v)

test_values = [0, 1, "", "0", [], [0], {}, None]

for value in test_values:
    print(f"Value: {repr(value)} -> Truthy: {is_truthy(value)}")