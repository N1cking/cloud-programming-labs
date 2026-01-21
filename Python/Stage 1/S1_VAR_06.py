import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from test_helper import eq


def to_int_or_none(s):
    if s is None:
        return None
    try:
        return int(s)
    except (ValueError, TypeError):
        return None


print(to_int_or_none("12"))
print(to_int_or_none(" 12 "))
print(to_int_or_none("12x"))
print(to_int_or_none(""))
print(to_int_or_none(None))

eq(to_int_or_none("12"), 12)
eq(to_int_or_none(" 12 "), 12)
