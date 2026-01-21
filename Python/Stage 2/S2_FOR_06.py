def sum_nested(matrix):
    total = 0
    for row in matrix:
        if not isinstance(row, list):
            return None
        for value in row:
            total += value
    return total


print(sum_nested([[1, 2], [3, 4]]))
print(sum_nested([[1], "x", [2]]))
