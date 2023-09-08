def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'палатка': 5, 'вода': 3, 'консервы': 4, 'сменная одежда': 2, 'аптечка': 1}
max_weight = 10
print(pack_backpack(items, max_weight))