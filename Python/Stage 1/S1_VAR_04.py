a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True, values are the same
print(f"a is b: {a is b}")  # False, different objects
print(f"a is c: {a is c}")  # True, same object

# Use is for identity, == for equality.
nothing = None
print(f"nothing is None: {nothing is None}")  # Correct identity check
