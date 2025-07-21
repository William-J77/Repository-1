

# spells = {"Fireball": 80, "Ice Blast": 70, "Lightning": 90}

# def boost_spell(spell_dict):
#     while True:
#         boost_sp = input("\nWhich spell would you like to boost?(Type 'done' to quit) ").strip().title()
#         if boost_sp in spell_dict:
#             boost_amount = int(input(f"How much would you like to boost {boost_sp}? "))
#             spell_dict[boost_sp] += boost_amount # spell_dict["Fireball"] = spell_dict["Fireball"] + boost_amount
                             # += adds something to a variable’s current value and then reassigns that new value back to the variable.
#             for spell, value in spell_dict.items():
#                 print(f"{spell} has a value of {value}.")
#         elif boost_sp == "Done":
#             print("Good bye!")
#             break
#         else:
#             print(f"{boost_sp} not found.")

# boost_spell(spells)



# To block out whole area of code use command + /



# Enchanted Shop: Price Updater

# shop_items = {"Potion": 50, "Elixir": 100, "Scroll": 75}

# def update_price(item_list):
#     while True:
#         item_update = input("\nWhat item would you like to update the price on?(Type 'done' to quit) ").strip().title()
#         if item_update in item_list:
#             price_change = int(input(f"How much would you like to add or subtract from the price of {item_update}?(20 or -20 etc...) "))
#             item_list[item_update] += price_change #the change/integer goes last here
#             for item, value in item_list.items():
#                 print(f"\n{item} has a value of {value}.")
#         elif item_update == "Done":
#             print("Good bye!")
#             break
#         else:
#             print("Error. Item not found")

# update_price(shop_items)



# Enchanted Inventory Tracker

scrolls = {"Destiny": 5, "Strength": 10, "Agility": 10}

def inventory_change(scroll_list):
    while True:
        print(f"\n{scrolls}")
        i_update = input("\nWhich scroll inventory would you like to update? (Type 'done' to quit) ").strip().title()
        if i_update == "Done":
            print("Good bye!")
            break
        elif i_update in scroll_list:
            amount = int(input(f"What is the change to {i_update}? (2 or -2 etc...) "))
            scroll_list[i_update] += amount
            for scroll, quantity in scroll_list.items():
                print(f"\n{quantity} of {scroll} scrolls.")
        else:
            print(f"{i_update} is an invalid choice. Please try again.")

inventory_change(scrolls)
