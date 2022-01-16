from art import coffee_machine_art, coffe_cup

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


print(coffee_machine_art)

print('-------------------------')
print('-------------------------')


print('Please select your coffe from MENU:')

print('Espresso $1.50')
print('Latte $2.50')
print('Cappucino $3')


print('-------------------------')

water = resources['water']
coffee = resources['coffee']
milk = resources['milk']

coffee_machine_on = True

money = float(0)
espresso_price = MENU['espresso']['cost']
latte_price = MENU['latte']['cost']
cappuccino_price = MENU['cappuccino']['cost']

def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def coins():
    """Returns value of coints inserted"""
    print('Please insert coints ')
    quarters = int(input('How many quarters? ')) * 0.25
    dimer = int(input('How many dimes? ')) * 0.10
    nickles = int(input('How many nickles? ')) * 0.05
    pennies = int(input('How many pennies? ')) * 0.01
    return float(quarters + dimer + nickles + pennies)


def check_transaction(money_inserted, drink_cost):
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def Coffee_machine():
    global coffee_machine_on
    coffee_machine_on = True
    global money
    while coffee_machine_on:
        choice = input("​What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            coffee_machine_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = coins()
                if check_transaction(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


Coffee_machine()
