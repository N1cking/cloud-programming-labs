def stats(nums):
    if not nums:
        return None

    total = sum(nums)
    return {
        "min": min(nums),
        "max": max(nums),
        "avg": total / len(nums),
        "sum": total,
    }


print(stats([1, 2, 3]))
print(stats([-5, 0, 5]))
print(stats([]))
