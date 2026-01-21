def parse_line(line):
    try:
        level_part, rest = line.split(":", 1)
        level = level_part.strip()
        pieces = rest.strip().split()
        data = {"level": level}
        for piece in pieces:
            if "=" in piece:
                key, value = piece.split("=", 1)
                data[key] = value
        return data
    except ValueError:
        return None


lines = [
    "INFO: user=42 action=login",
    "DEBUG: user=11 action=logout",
    "INFO: user=abc action=login",
    "INFO: user=7 action=checkout",
]

parsed = [parse_line(line) for line in lines]
info_only = [item for item in parsed if item and item.get("level") == "INFO"]
user_ids = []
for item in info_only:
    try:
        user_ids.append(int(item.get("user", "")))
    except ValueError:
        continue

print(user_ids)
