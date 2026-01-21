def pipe_safe(*fns):
    def apply(value):
        result = value
        try:
            for fn in fns:
                result = fn(result)
            return {"ok": True, "value": result}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    return apply


def inverse(n):
    if n == 0:
        raise ValueError("division by zero")
    return 1 / n


safe = pipe_safe(lambda x: x + 1, inverse)
print(safe(1))
print(safe(-1))
