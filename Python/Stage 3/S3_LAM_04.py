nums = [1, 2, 3, 4, 5, 6]

filtered = list(filter(lambda n: n % 2 == 0, nums))
squares = list(map(lambda n: n * n, filtered))
result = sum(squares)

print("evens:", filtered)
print("squares:", squares)
print("sum:", result)
