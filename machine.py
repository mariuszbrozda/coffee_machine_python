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



# TODO 1  Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​

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

coffe_machine_on = True

while coffe_machine_on True:
    coffe_type = input('​What would you like? (espresso/latte/cappuccino)').lower()




money = float(0)
espresso_price = MENU['espresso']['cost']
latte_price = MENU['latte']['cost']
cappuccino_price = MENU['cappuccino']['cost']


def coints():
    quarters = float(input('How many quarters? ')) * 0.25
    dimer = float(input('How many dimes? ')) * 0.10
    nickles = float(input('How many nickles? ')) * 0.05
    pennies = float(input('How many pennies? ')) * 0.01
    return float(quarters + dimer + nickles + pennies)

def make_espresso(water, coffee, money_inserted):
    money_inserted = coints()

    water -= 50
    coffee -= 18
    print(f'money collected {money_inserted}')
    money_inserted -= MENU["espresso"]['cost']
    print(f'Here is your change: {money_inserted}')
    print(coffe_cup)
    print('Thank you, your EXPRESSO is ready! Have a nice day!')

def make_latte(water, coffee, milk,):
    money_inserted = coints()
    print(f'money inserted ${money_inserted}')
    water -= 200
    coffee -= 24
    milk -= 150
    money_inserted -= MENU["latte"]['cost']
    print(f'Here is your change: {money_inserted}')
    print(coffe_cup)
    print('Thank you, your LATTE is ready! Have a nice day!')

def make_cappuccino(water, coffee, milk,):
    money_inserted = coints()
    water -= 250
    coffee -= 24
    milk -= 100
    money_inserted -= MENU["cappuccino"]['cost']
    print(f'money inserted ${money_inserted}')
    print(f'Here is your change: {money_inserted}')
    print(coffe_cup)
    print('Thank you your CAPPUCINO is ready! Have a nice day!')

def check_transaction(money_inserted, espresso_price, latte_price, cappuccino_price, money):
    if money_inserted < espresso_price:
        print("​Sorry that's not enough money. Money refunded.​")
        coffe_machine_on = False
    else:
        money += MENU["espresso"]['cost']

    if money_inserted < latte_price:
        print("​Sorry that's not enough money. Money refunded.​")
        coffe_machine_on = False
    else:
        money += MENU["latte"]['cost']

    if money_inserted < cappuccino_price:
        print("​Sorry that's not enough money. Money refunded.​")
        coffe_machine_on = False
    else:
        money += MENU["cappuccino"]['cost']