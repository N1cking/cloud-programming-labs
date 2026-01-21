people = [
    {"name": "Ola", "age": 31},
    {"name": "Max", "age": 22},
    {"name": "Zoe", "age": 27},
]

print("before:", people)
print("after:", sorted(people, key=lambda p: p["age"]))
