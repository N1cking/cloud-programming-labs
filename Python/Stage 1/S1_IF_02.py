def grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return None

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


for s in [59, 60, 69, 70, 89, 90, 100, 101]:
    print(s, grade(s))
