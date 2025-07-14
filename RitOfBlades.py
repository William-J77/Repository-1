

weap_tool_list = []
sharpen_amount = []

print("\nWhat Weapons or Tools would you like to sharpen today?\n")

for i in range(4):
    weap_tool = input(f"Weapon or Tool #{i + 1}: ").strip().lower()
    weap_tool_list.append(weap_tool)
    sharpen = int(input(f"How many times to sharpen {weap_tool}? "))
    sharpen_amount.append(sharpen)

for i in range(len(weap_tool_list)-1, -1, -1):
    print(f"Bringing the {weap_tool_list[i]} to the grindstone.")
    for _ in range(sharpen_amount[i]):
        print("Sharpening!")

print(f"\nFinished sharpening these weapons/tools:\n{' '.join(weap_tool_list)}")
