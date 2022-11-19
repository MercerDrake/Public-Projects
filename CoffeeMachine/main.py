MENU = {
    "Espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.50,
    },
    "Latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.50,
    },
    "Cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}


def printReport():
    for key, value in resources.items():
        if key == "Water" or key == "Milk":
            print(f"{key}: {value}ml")
        elif key == "Coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: ${value}")


def checkResources(selection):
    for key in MENU[selection]["ingredients"].keys():
        if MENU[selection]["ingredients"][key] <= resources[key]:
            sufficientIngredients = True
        else:
            sufficientIngredients = False
            print(f"Sorry there isn't enough {key} for that.")
            return
    processCoins(selection)


def processCoins(selection):
    print(f"Please input coins.")
    total = int(input("Number of quarters: ")) * 0.25
    total += int(input("Number of dimes: ")) * 0.10
    total += int(input("Number of nickels: ")) * 0.05
    total += int(input("Number of pennies: ")) * 0.01
    total = round(total, 2)
    transactionSuccessful(selection, total)


def transactionSuccessful(selection, total):
    if MENU[selection]["cost"] <= total:
        change = total - MENU[selection]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        resources["Money"] += MENU[selection]["cost"]
        makeCoffee(selection)
    else:
        print(f"Sorry, that's not enough money. ${total} refunded.")


def makeCoffee(selection):
    for key, value in MENU[selection]["ingredients"].items():
        resources[key] -= value
    print(f"Here is your {selection}. Enjoy!")


on = True
while on:
    selection = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if selection == "Off":
        on = False
    elif selection == "Espresso" or selection == "Latte" or selection == "Cappuccino":
        checkResources(selection)
    elif selection == "Report":
        printReport()
    else:
        print(f"Sorry, that is not a valid selection.")
