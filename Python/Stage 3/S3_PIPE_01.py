def pipe(*fns):
    def apply(value):
        result = value
        for fn in fns:
            result = fn(result)
        return result

    return apply


add2 = lambda n: n + 2
mul3 = lambda n: n * 3
sub1 = lambda n: n - 1

pipeline = pipe(add2, mul3, sub1)
print(pipeline(4))
