# =================================
# Classwork for 11DTE: Mni-project by Zade Viggers is licensed under Attribution-ShareAlike 4.0 International.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
# Check the LICENSE.md file for more details.
# =================================
import random

# Constants
MAX_COFFEE_COUNT = 10  # The maximum number of coffees that can be ordered
# The default amount of coffees ordered if the user does not select an amount
DEFAULT_COFFEE_AMOUNT = 1

coffee_menu = ["mocha", "cappuccino", "expresso",
               "latte", "flat white"]  # List of avalible Coffees
coffee_price_menu = [15, 12,
                     14, 13.50, 16]  # List of coffee prices (in NZD)


# The maximunm amount of each coffee that can be ordered
maximum_ammount_of_coffees_menu = [2, 2, 3, 4, 7]

# Variables
order = []  # The order will be placed in this variable
total_price = 0  # This variable will be used to keep track of the total price of the order

print("Welcome to the Coffee shop!")
print("Please place your order.")

ordering = True  # Used to keep track of if the user is placing an order
# Loop that collects and order from people then asks if they want another one and if they do it keeps going and if they don't the loop exits
while ordering:
    vaild_coffe_type_input = False
    # Loop that runs until the user provides a valid input
    while not vaild_coffe_type_input:
        print()  # New line
        # Print out a list of all the avalible coffees by looping therough both the price and item menus at the same time using the zip() method
        for coffee, price in zip(coffee_menu, coffee_price_menu):
            print(" - {} (${:.2f})".format(coffee.title(), price))
        print()  # New line

        coffee_type_input = input(
            "Please choose your coffee type from the list above: ").strip().lower()  # Ask the user what coffee they want

        # Make sure that it's a valid coffee type
        if coffee_type_input not in coffee_menu:
            print("Please select a valid coffee type!")
        else:

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
                        # Make sure the user inputs a number greater than 0
                        if ammount_of_coffee < 1:
                            print("You can't order less than 1 coffee!")
                        else:
                            # Make sure that the user doesn't input more than the maximunm for that coffee type
                            maximun_ammount_of_this_coffee = maximum_ammount_of_coffees_menu[coffee_menu.index(
                                coffee_type_input)]
                            if ammount_of_coffee > maximun_ammount_of_this_coffee:
                                print("You can't order more than {} {}s!".format(
                                    maximun_ammount_of_this_coffee, coffee_type_input))
                            else:

                                # Add the coffee to the order
                                order.append([coffee_type_input, ammount_of_coffee])
                                ammount_of_coffee_vaild = True
                    except ValueError:
                        print("Please select a valid number of coffees!")
                        continue  # Continue looping, but end this iteration of the loop
            vaild_coffe_type_input = True

        # Add a random coffee to the order
        random_coffee = random.choice(coffee_menu)
        order.append([random_coffee, 1])

        # Check if the user wants to ad another coffee to the order
        wants_another_coffee = input(
            "Do you want to add another coffee to the order? (yes/no): ").strip().lower()  # Get input from user

        # Default to no if thgey don't provide a valid option
        if len(wants_another_coffee) == 0 or wants_another_coffee not in ["y", "yes", "n", "no"]:
            print("Valid option not selected. Defaulting to no.")
            ordering = False
        # If the user does not input yes(i.e. no or n), then end this iuteration of the loop
        elif wants_another_coffee != "yes" and wants_another_coffee != "y":
            ordering = False



# Print the final order
print("\nHere is your final order:\n")
# loop through each item in the order
for item in order:

    total_price += coffee_price_menu[coffee_menu.index(
        item[0])]*item[1]  # Add the price of this coffee to the total price

    print("{}x {} - ${} (${} each)".format(item[1], item[0].title(), coffee_price_menu[coffee_menu.index(
        item[0])]*item[1], coffee_price_menu[coffee_menu.index(item[0])]))  # Print this item out


print("Total price: ${}".format(total_price))  # Print total price
print("\nThank you for your buisness!")
