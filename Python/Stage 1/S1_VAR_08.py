big_int = 10**100

print("big_int type:", type(big_int).__name__)
print("digits:", len(str(big_int)))

big_float = float(big_int)
print("big_float:", big_float)
# Large floats lose precision because they use fixed-size binary representation.
