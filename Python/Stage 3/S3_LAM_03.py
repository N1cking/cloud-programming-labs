def make_adder(x):
    return lambda n: n + x


add10 = make_adder(10)
add3 = make_adder(3)

print(add10(5))
print(add10(-2))
print(add3(7))
