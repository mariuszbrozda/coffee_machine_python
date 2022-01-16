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
