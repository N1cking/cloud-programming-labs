def compose(*fns):
    def apply(value):
        result = value
        for fn in reversed(fns):
            result = fn(result)
        return result

    return apply


add2 = lambda n: n + 2
mul3 = lambda n: n * 3
sub1 = lambda n: n - 1

piped = lambda x: sub1(mul3(add2(x)))
composed = compose(sub1, mul3, add2)

print(piped(4))
print(composed(4))
