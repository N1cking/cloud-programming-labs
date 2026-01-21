import math

nan1 = float("nan")

try:
    nan2 = 0.0 / 0.0
except ZeroDivisionError:
    nan2 = float("nan")

print(f"nan1 == nan1: {nan1 == nan1}")
print(f"nan2 == nan2: {nan2 == nan2}")
print(f"isnan(nan1): {math.isnan(nan1)}")
print(f"isnan(nan2): {math.isnan(nan2)}")
