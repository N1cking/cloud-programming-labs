def active_names(users):
    names = [user["name"].upper() for user in users if user.get("active")]
    return sorted(names)


users = [
    {"id": 1, "name": "Ola", "active": True},
    {"id": 2, "name": "Max", "active": False},
    {"id": 3, "name": "Zoe", "active": True},
]

print(active_names(users))
