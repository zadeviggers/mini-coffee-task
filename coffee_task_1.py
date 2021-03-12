# =================================
# Classwork for 11DTE: Mni-project by Zade Viggers is licensed under Attribution-ShareAlike 4.0 International.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
# Check the LICENSE.md file for more details.
# =================================

# Constants
MAX_COFFEE_COUNT = 3
DEFAULT_COFFEE_AMOUNT = 1

coffee_menu = ["mocha", "cappuccino", "expresso",
               "latte", "flat white"]  # List of avalible Coffees
coffee_price_menu = [15, 12,
                     14, 13.50, 16]  # List of coffee prices (in NZD)

# Variables
order = []
total_price = 0

print("welcome to the Coffee shop!")
print("Pleas place your order.")


vaild_coffe_type_input = False
while not vaild_coffe_type_input:
    print()  # New line
    for coffee, price in zip(coffee_menu, coffee_price_menu):
        print(" - {} (${})".format(coffee, price))
    print()  # New line

    coffee_type_input = input(
        "Please choose your coffee type from the list above: ").strip().lower()
    if coffee_type_input not in coffee_menu:
        print("Please select a valid coffee type!")
        continue  # Continue looping, but end this iteration of the loop

    ammount_of_coffee_vaild = False
    while not ammount_of_coffee_vaild:
        ammount_of_coffee = input(
            "How many {}s do you want? ".format(coffee_type_input)).strip().lower()

        try:
            ammount_of_coffee = int(ammount_of_coffee)
        except ValueError:
            print("Please select a valid number of coffees!")
            continue  # Continue looping, but end this iteration of the loop
        order.append([coffee_type_input, ammount_of_coffee])
        ammount_of_coffee_vaild = True

    vaild_coffe_type_input = True

print("\nHere is your final order:\n")
for item in order:
    total_price += coffee_price_menu[coffee_menu.index(
        item[0])]*item[1]
    print("{}x {} - ${} (${} each)".format(item[1], item[0], coffee_price_menu[coffee_menu.index(
        item[0])]*item[1], coffee_price_menu[coffee_menu.index(item[0])]))

print("Total price: ${}".format(total_price))
print("\nThank you for your buisness!")
