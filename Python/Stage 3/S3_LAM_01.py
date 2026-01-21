square = lambda n: n * n
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"

print(square(2))
print(square(5))
print(square(-3))

print(is_odd(1))
print(is_odd(2))
print(is_odd(9))

print(greet("Ola"))
print(greet("Max"))
print(greet("Zoe"))
