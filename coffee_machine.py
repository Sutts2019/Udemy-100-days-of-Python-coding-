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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

def print_report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: ${round(resources["money"],2)}")

def check_resources(water, milk, coffee):
    if resources["water"] - water <= 0:
        print("Sorry, not enough water")
        return False
    elif resources["milk"] - milk <= 0:
        print("Sorry, not enough milk")
        return False
    elif resources["coffee"] - coffee <= 0:
        print("Sorry, not enough coffee")
        return False
    else:
        return True

def enter_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?:"))
    total = sum((quarters * 0.25, dimes * 0.1, nickles * 0.05, pennies * 0.01))
    return total

def check_cost(cash, cost):
    if cash < cost:
        return False
    else:
        return True

def vend(user_choice):
    drink = user_choice
    # TODO: 4. Check sufficient resources for user request
    water = MENU[drink]["ingredients"]["water"]
    milk = MENU[drink]["ingredients"]["milk"]
    coffee = MENU[drink]["ingredients"]["coffee"]

    if check_resources(water, milk, coffee):
    # TODO: 5. Prompt user to enter coins and process coins (total amount)
        cash_entered = round(enter_coins(),2)
        print(f"You have entered: {cash_entered}")
    # TODO: 6. Check transaction successful? (payment amount sufficient, dispense change, add payment to resources
        drink_price = MENU[drink]["cost"]
        paid = check_cost(cash_entered, drink_price)
        if paid:
            print(f"Your {drink} cost ${drink_price}. You paid ${cash_entered}, change returned ${round(cash_entered - drink_price,2)}")
            print("Please enjoy your ☕.")
            resources["money"] += drink_price
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
        else:
            print("Insufficient funds entered, money has been returned")

#start machine
machine_on = True

while machine_on:
    # TODO: 1. Prompt user "What would you like? (Espresso/Latte/Cappuccino): "
    user_choice = input("What would you like? (espresso/latte/capuccino)").lower()
    # TODO: 2. Print report of all coffee machine resources
    if user_choice == "report":
        print_report()
    # TODO: 3. Turn off coffee machine by entering 'off' to prompt
    elif user_choice == "off":
        machine_on = False
        print("Powering down, thank you!")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        vend(user_choice)
    else:
        print("Invalid input, try again")

