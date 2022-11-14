import time

def printPause(message):
    print(message, flush = True)
    time.sleep(2)

def validInput(prompt, valid1, valid2):
    while True:
        response=input(prompt).lower()
        if valid1 in response:
            return response
        elif valid2 in response:
            return response
        else:
            printPause("Sorry, I don't understand.")

def intro():
    printPause("Hello! I am Bob, the Breakfast Bot.")
    printPause("Today we have two breakfasts available.")
    printPause("The first is waffles with strawberries and whipped cream.")
    printPause("The second is sweet potato pancakes with butter and syrup.")

def getOrder():
    response = validInput("Please place your order. "
                            "Would you like waffles or pancakes?\n",
                             "waffles", "pancakes")
    if "waffles" in response:
        printPause("Waffles it is!")
    elif "pancakes" in response:
        printPause("Pancakes it is!")
    printPause("Your order will be ready shortly.")
    orderAgain()

def orderAgain():
    order = validInput("Would you like to place another order? "
                            "Please say 'yes' or 'no'\n",
                            'no', 'yes')
    if 'no' in order:
        printPause("OK, goodbye!")
    elif 'yes' in order:
        printPause("Very good, I'm happy to take another order.")
        getOrder()

def orderBreakfast():
    intro()
    getOrder()
    orderAgain()

orderBreakfast()