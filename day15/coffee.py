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

turn_off = False

def process_coin():
    total = int(input('How many quarters? ')) * 0.25
    total += int(input('How many dimes? ')) * 0.10
    total += int(input('How many nickels? ')) * 0.05
    total += int(input('How many pennies? ')) * 0.01
    return total

def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Not sufficient {item}")
            return False
        else:
            return True

def process_transaction(coins, drink_cost):
    global profit
    if coins < drink_cost:
        print("Amount not sufficient, here's your refund")
        return False
    elif coins >= drink_cost:
        print(f"Here's your change {round(coins - drink_cost, 2)}")
        profit += drink_cost
        return profit

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Enjoy your {drink_name}")


profit = 0
        
while not turn_off:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == 'off':
        turn_off = True

    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")

    else:
        drink = MENU[choice]
        
        if is_resource_sufficient(drink['ingredients']): 
            coins = process_coin()
            if process_transaction(coins, drink['cost']):
                make_coffee(choice, drink['ingredients'])