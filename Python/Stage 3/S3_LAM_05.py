def at_least(min_value):
    return lambda n: n >= min_value


nums = [1, 3, 5, 7, 9]
filtered = list(filter(at_least(5), nums))
print(filtered)
