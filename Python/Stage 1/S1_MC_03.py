def calc(a, op, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


print(calc(2, "+", 3))
print(calc(10, "-", 4))
print(calc(3, "*", 5))
print(calc(10, "/", 2))
print(calc(10, "/", 0))
print(calc("2", "+", 3))
