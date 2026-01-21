def count_occurrences(values):
    counts = {}
    for item in values:
        counts[item] = counts.get(item, 0) + 1
    return counts


print(count_occurrences(["a", "b", "a", "c", "b", "a"]))
