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


input_money = 0
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
money = 0


def cents():
    global custom_quarters
    global custom_dimes
    global custom_nickles
    global custom_pennies
    custom_quarters = int(input("How many quarters?: "))
    custom_dimes = int(input("How many dimes?: "))
    custom_nickles = int(input("How many nickles?: "))
    custom_pennies = int(input("How many pennies?: "))


def count_change(coffee):
    global count_finish
    change = input_money - MENU[coffee]["cost"]
    if change == 0:
        print(f"Here is your {coffee}. Enjoy!")
        count_finish = True
    elif change > 0:
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {coffee}. Enjoy!")
        count_finish = True
    else:
        count_finish = False
        change *= -1
        print(f"There is not enough money. Need to input {round(change, 2)}")
        cents()


def count_resources(coffee):
    global money
    if coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        money += MENU[coffee]["cost"]
    elif coffee == "latte" or coffee == "cappuccino":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        money += MENU[coffee]["cost"]


finish = False
while finish is False:
    report = f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
    order = input("What would you like? (espresso/latte/cappuccino):  ")
    if order == "report":
        print(report)
    elif order == "espresso":
        count_resources("espresso")
        if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
            print("There is not enough ingredients. Come tomorrow")
            finish = True
        else:
            print("Please, insert coins.")
            cents()
            count_cents = (penny * custom_pennies + nickel * custom_nickles + dime * custom_dimes + quarter * custom_quarters)
            input_money = 0
            input_money += count_cents
            count_finish = False
            while count_finish is False:
                count_change(coffee="espresso")
                input_money += count_cents

    elif order == "latte":
        count_resources("latte")
        if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
            print("There is not enough ingredients. Come tomorrow")
            finish = True
        else:
            print("Please, insert coins.")
            cents()
            count_cents = (penny * custom_pennies + nickel * custom_nickles + dime * custom_dimes + quarter * custom_quarters)
            input_money = 0
            input_money += count_cents
            count_finish = False
            while count_finish is False:
                count_change(coffee="latte")
                input_money += count_cents

    elif order == "cappuccino":
        count_resources("cappuccino")
        if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
            print("There is not enough ingredients. Come tomorrow")
            finish = True
        else:
            print("Please, insert coins.")
            cents()
            count_cents = (penny * custom_pennies + nickel * custom_nickles + dime * custom_dimes + quarter * custom_quarters)
            input_money = 0
            input_money += count_cents
            count_finish = False
            while count_finish is False:
                count_change(coffee="cappuccino")
                input_money += count_cents
    elif order == "off":
        finish = True
        print("Process is finished")