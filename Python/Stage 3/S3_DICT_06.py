def group_by(items, key):
    grouped = {}
    for item in items:
        value = item.get(key)
        grouped.setdefault(value, []).append(item)
    return grouped


items = [
    {"id": 1, "team": "red"},
    {"id": 2, "team": "blue"},
    {"id": 3, "team": "red"},
]

print(group_by(items, "team"))
