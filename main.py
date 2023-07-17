MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report of all coffee machine resources.
# TODO: 2. Check resources sufficient to make drink order.
# TODO: 3. Process coins.
# TODO: 4. Check transaction successful.
# TODO: 5. Make coffee!

earnings = 0

machine_on = True


def check_resources(choice_ingredients):
    """Returns True if order can be made, False if ingredients are insufficient."""
    for ingredient in choice_ingredients:
        if choice_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient}. ")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(coins_inserted, drink_cost):
    """Return True if payment is accepted, False if money is insufficient."""
    if coins_inserted >= drink_cost:
        change = round(coins_inserted - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global earnings
        earnings += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded. ")
        return False


def deduct_ingredients(drink_name, choice_ingredients):
    """Deduct the ingredients from the resources."""
    for ingredient in choice_ingredients:
        resources[ingredient] -= choice_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕. Enjoy! ")


while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g "
              f"\nMoney: ${earnings}")
    elif choice == "off":
        print("Maintenance mode. Machine will turn off. ")
        machine_on = False
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                deduct_ingredients(choice, drink["ingredients"])

# TODO: 6. Check user input!! (Coming soon)







