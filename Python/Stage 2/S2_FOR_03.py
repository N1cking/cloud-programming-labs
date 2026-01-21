def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total


print(sum_until([1, 2, 3, 4, 5], 7))
print(sum_until([5, 5, 5], 10))
