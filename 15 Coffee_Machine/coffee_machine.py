MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0
}


def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}")


def collect_money():
    """ Returns the total of the coins inserted."""
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total = quarter*0.25 + dime*0.10 + nickel*0.05 + penny*0.01
    return total


def is_money_enough(money, coffee_type):
    """Checks if the money inserted is enough or not"""
    coffee_cost = MENU[f"{coffee_type}"]["cost"]
    if money == coffee_cost:
        resources['money'] += coffee_cost
        return True
    elif money > coffee_cost:
        print(f"Here is {(money-coffee_cost):.02f}$ in change.")
        resources['money'] += coffee_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def is_resources_available(ingredients):
    """Check if there are enough resources for given order"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"There's not enough {item}.")
            return False
    return True


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'off:':
        break
    elif user_input == 'report':
        report()
    else:
        valid_resource = is_resources_available(MENU[f"{user_input}"]['ingredients'])
        if valid_resource:
            user_money = collect_money()
            payment_successful = is_money_enough(user_money, user_input)
            if payment_successful:
                print(f"Here is your {user_input}. Enjoy!")
