# =================================
# Classwork for 11DTE: Mni-project by Zade Viggers is licensed under Attribution-ShareAlike 4.0 International.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
# Check the LICENSE.md file for more details.
# =================================
import random

# Constants
MAX_COFFEE_COUNT = 3
DEFAULT_COFFEE_AMOUNT = 1

coffee_menu = ["mocha", "cappuccino", "expresso",
               "latte", "flat white"]  # List of avalible Coffees
coffee_price_menu = [15, 12,
                     14, 13.50, 16]  # List of coffee prices (in NZD)

# The maximunm amount of each coffee that can be ordered
maximum_ammount_of_coffees_menu = [2, 2, 3, 4, 7]

# Variables
order = []
total_price = 0

print("Welcome to the Coffee shop!")
print("Pleas place your order.")


ordering = True
while ordering:
    vaild_coffe_type_input = False
    while not vaild_coffe_type_input:
        print()  # New line
        for coffee, price in zip(coffee_menu, coffee_price_menu):
            print(" - {} (${})".format(coffee.title(), price))
        print()  # New line

        coffee_type_input = input(
            "Please choose your coffee type from the list above: ").strip().lower()

        if coffee_type_input not in coffee_menu:
            print("Please select a valid coffee type!")
            continue  # Continue looping, but end this iteration of the loop

        # Loop until the user provides a valid ammount of coffee, OR they provide no input, in which case it defaults to 1
        ammount_of_coffee_vaild = False
        while not ammount_of_coffee_vaild:
            ammount_of_coffee = input(
                "How many {}s do you want? ".format(coffee_type_input.title())).strip().lower()

            # Default to 1 coffee if the user inputs nothing
            if len(ammount_of_coffee) == 0:
                ammount_of_coffee = 1
                print("Amount not provided. Defaulting to 1.")
            else:
                # Make sure the input is a valid number
                try:
                    ammount_of_coffee = int(ammount_of_coffee)
                except ValueError:
                    print("Please select a valid number of coffees!")
                    continue  # Continue looping, but end this iteration of the loop

            # Make sure the user inputs a number greater than 0
            if ammount_of_coffee < 1:
                print("You can't order less than 1 coffee!")
                continue  # Continue looping, but end this iteration of the loop

            # Make sure that the user doesn't input more than the maximunm for that coffee type
            maximun_ammount_of_this_coffee = maximum_ammount_of_coffees_menu[coffee_menu.index(
                coffee_type_input)]
            if ammount_of_coffee > maximun_ammount_of_this_coffee:
                print("You can't ordxer more than {} {}s!".format(
                    maximun_ammount_of_this_coffee, coffee_type_input))
                continue  # Continue looping, but end this iteration of the loop

            # Add the coffee to the order
            order.append([coffee_type_input, ammount_of_coffee])
            ammount_of_coffee_vaild = True

        vaild_coffe_type_input = True
    wants_another_coffee = input(
        "Do you want to add another coffee to the order? (yes/no): ").strip().lower()
    if not (wants_another_coffee == "yes" or wants_another_coffee == "y"):
        ordering = False
        continue  # Continue looping, but end this iteration of the loop

# Add a random coffee to the order
random_coffee = random.choice(coffee_menu)
order.append(
    [random_coffee, 1])


print("\nHere is your final order:\n")
for item in order:
    total_price += coffee_price_menu[coffee_menu.index(
        item[0])]*item[1]
    print("{}x {} - ${} (${} each)".format(item[1], item[0].title(), coffee_price_menu[coffee_menu.index(
        item[0])]*item[1], coffee_price_menu[coffee_menu.index(item[0])]))

print("Total price: ${}".format(total_price))
print("\nThank you for your buisness!")
