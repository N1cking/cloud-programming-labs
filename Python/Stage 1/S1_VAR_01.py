variables = {
    "int": 42,
    "float": 3.14,
    "str": "Hello",
    "bool": True,
    "None": None,
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "dict": {"a": 1, "b": 2},
    "set": {1, 2, 3},
    "function": lambda x: x
}

print(f"{'name':<10}{'value':<20}{'type(x)':<20}{'type(x).__name__'}")
for name, value in variables.items():
    print(f"{name:<10}{value!r:<20}{type(value):<20}{type(value).__name__}")