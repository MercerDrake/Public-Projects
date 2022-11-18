MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0.0
}


def userSelection():
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "off":
        return selection
    elif selection == "report":
        printReport()
    else:
        checkResources(selection)


def checkResources(selection):


def processCoins():
    print(f"Please insert coins.")
    numOfQuarters = input("How many quarters?: ")
    numOfDimes = input("How many dimes?: ")
    numOfNickles = input("How many nickles?: ")
    numOfPennies = input("How many pennies?: ")
    total = ((int(numOfQuarters) * 0.25) + (int(numOfDimes) * 0.10) +
             (int(numOfNickles) * 0.05) + (int(numOfPennies) * 0.01))
    return total


def checkTransaction(selection):
    total = processCoins()
    if total >= MENU[selection]["cost"]:
        if total > MENU[selection]["cost"]:
            change = total - MENU[selection]["cost"]
            resources["Money"] += MENU[selection]["cost"]
            print(f"Here is {change} in change")
            makeCoffee(selection)
    elif total < MENU[selection]["cost"]:
        print(f"Sorry, that's not enough money. ${total} refunded.")


def makeCoffee(selection):
    if selection == "espresso":
        resources["Coffee"] -= MENU[selection]["ingredients"]["Coffee"]
        resources["Water"] -= MENU[selection]["ingredients"]["Water"]
    elif selection == "cappuccino" or selection == "latte":
        resources["Coffee"] -= MENU[selection]["ingredients"]["Coffee"]
        resources["Water"] -= MENU[selection]["ingredients"]["Water"]
        resources["Milk"] -= MENU[selection]["ingredients"]["Milk"]
    print(f"Here is your {selection}. Enjoy!")


def printReport():
    for key, value in resources.items():
        if key == "Water" or key == "Milk":
            print(f"{key}: {value}ml")
        elif key == "Coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: ${value}")


on = True
while (on == True):
    selection = userSelection()
    if selection == "off":
        on = False
