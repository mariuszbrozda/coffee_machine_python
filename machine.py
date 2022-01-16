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

def Coffee_machine(coffe_type, money, resources, water, coffee, milk):
    # money = float(0)
    if coffe_type == 'espresso':
        # price 1.50$
        # 50 ml Water
        # 18g coffee
        price = 1.50
# TODO 3 Check resources sufficient?
        if water >= 50:
            print('enough respirces to make an coffee')
            check_transaction(money_inserted, espresso_price, latte_price, cappuccino_price, money)
            make_espresso(water, coffee)
        else:
            print(f'Sorry there is not sufficient resources. Please refill water ')

        if coffee >= 18:
            print('enough respirces to make an coffee')
            check_transaction(money_inserted, espresso_price, latte_price, cappuccino_price, money)
            make_espresso(water, coffee,)
        else:
            print(f'Sorry there is not sufficient resources. Please refill coffee ')
    elif coffe_type == 'latte':
        # price 2.50$
        # 200ml water
        # 24g coffee
        # 150ml milk
        if water > 200:
            check_transaction(money_inserted, espresso_price, latte_price, cappuccino_price, money)
            make_latte(water, coffee, milk)
        else:
            print('Sorry there is not sufficient resources. Please refill water')

        if coffee > 24:
            check_transaction(money_inserted, espresso_price, latte_price, cappuccino_price, money)
            make_latte(water, coffee, milk)
        else:
            print('Sorry there is not sufficient resources. Please refill Coffee')

        if milk > 150:
            check_transaction(money_inserted, espresso_price, latte_price, cappuccino_price, money)
            make_latte(water, coffee, milk)
        else:
            print('Sorry there is not sufficient resources. Please refill milk')
    elif coffe_type == 'cappuccino':
        # price 3$
        # 250ml water
        # 24g coffee
        # 100ml milk
        if water >= 250:
            make_cappuccino(water, coffee, milk)
        else:
            print('Sorry there is not sufficient resources. Please refill water')

        if coffee >= 24:
            make_cappuccino(water, coffee, milk)
        else:
            print('Sorry there is not sufficient resources. Please refill coffee')

        if milk >= 100:
            make_cappuccino(water, coffee, milk)
        else:
            print('Sorry there is not sufficient resources. Please refill coffee')

# TODO 2 Turn off the Coffee Machine by entering “​off”​to the prompt.
    elif coffe_type == 'off':
        coffe_machine_on = False
        print('Machine is OFF - Maintenance MODE')
# TODO 3 Print report.
    elif coffe_type == 'report':
        print('RESOURCES: ')
        print(f'WATER: {water}ml')
        print(f'MILK: {milk}ml')
        print(f'COFFEE: {coffee}g')
        print(f'MONEY: ${money}')
    else:
        print('Please select coffee type')

Coffee_machine(coffe_type, money, resources, water, coffee, milk)
