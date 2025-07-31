


treasure_chest = [
    {"name": "ruby", "value": 100, "magic": True,},
    {"name": "gold", "value": 200, "magic": False,},
    {"name": "silver", "value": 50, "magic": False,},
    {"name": "diamond", "value": 300, "magic": True}
]

for treasure in treasure_chest:
    name = treasure["name"]
    value = treasure["value"]
    magic = treasure["magic"]
    print(f"{name} is worth {value} and have a magic status of {magic}.")