from pprint import pprint


def inspect(v):
    try:
        iter(v)
        is_iterable = True
    except TypeError:
        is_iterable = False

    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": is_iterable,
        "truthy": bool(v),
    }


values = [
    0,
    1,
    "",
    "0",
    [],
    [0],
    {},
    None,
    (1, 2),
    lambda x: x,
]

results = [inspect(v) for v in values]
pprint(results)
