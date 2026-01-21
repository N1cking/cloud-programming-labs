lst = [1, 2, 3]
lst[0] = 10
print("Modified list:", lst)

try:
    tup = (1, 2, 3)
    tup[0] = 10  # This will raise an error
except TypeError as e:
    print("Error with tuple:", e)

# Explanation
print("\nA list is mutable, meaning its elements can be changed.")
print("A tuple is immutable, meaning its elements cannot be changed.")