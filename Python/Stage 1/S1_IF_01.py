def shipping_cost(weight_kg, is_member):
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return None

    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8

    return cost


print(shipping_cost(0.5, False))
print(shipping_cost(1, True))
print(shipping_cost(1.1, False))
print(shipping_cost(5, True))
print(shipping_cost(5.1, False))
print(shipping_cost("2", False))
