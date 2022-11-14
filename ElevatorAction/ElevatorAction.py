import time

def printPause(messageToPrint):
    print(messageToPrint)
    time.sleep(1)

def intro():
    printPause("You have just arrived at your new job!")
    printPause("You are in the elevator.")

def floorSelection(items):
    floor = input("Please enter the number for the floor you'd like to visit:\n"
                    " 1. Lobby\n 2. Human Resources\n 3. Engineering Department\n").lower()
    if "1" in floor or "lobby" in floor:
        firstFloor(items)
    elif "2" in floor or "human resources" in floor:
        secondFloor(items)
    elif "3" in floor or "engineering department" in floor:
        thirdFloor(items)
    
def firstFloor(items):
    printPause("You push the button for the first floor.")
    printPause("After a few moments, you find yourself in the lobby.")
    if "ID Card" not in items:
        printPause("The clerk greets you and gives you your ID Card")
        items.append("ID Card")
    elif "ID Card" in items:
        printPause("The clerk greets you, but she has already given you your\n"
        "ID Card, so there is nothing more to do here now.")
    printPause("You head back to the elevator.")
    floorSelection(items)

def secondFloor(items):
    printPause("You push the button for the second floor.")
    printPause("After a few moments, you find yourself in the human resources department")
    if "Handbook" not in items:
        printPause("The head of HR greets you.")
        if "ID Card" not in items:
            printPause("He has something for you, but says he can't\n"
            "give it to you until you get your ID Card.")
        elif "ID Card" in items:
            printPause("He looks at your ID Card and then gives you a copy of the Employee Handbook.")
            items.append("Handbook")
    elif "Handbook" in items:
        printPause("The folks in HR are busy at their desks.")
        printPause("There doesn't seem to be much to do here.")
    printPause("You head back to the elevator.")
    floorSelection(items)

def thirdFloor(items):
    printPause("You push the button for the third floor.")
    printPause("After a few moments, you find yourself in the engineering department.")
    if "ID Card" not in items:
        printPause("Unfortunately, the door is locked and you can't get it.")
        printPause("It looks like you need some kind of keycard to open the door.")
        printPause("You head back to the elevator.")
        floorSelection(items)
    elif "ID Card" in items:
        printPause("You use your ID Card to open the door.")
        printPause("Your program manager greets you and tells you that you need to have\n a copy of the employee handbook.")
        if "Handbook" not in items:
            printPause("They scowl when they see that you don't have it,\n and send you back to the elevator.")
            floorSelection(items)
        else:
            printPause("Fortunately, you got it from HR!\n")
            printPause("Congratulations! You are ready to start your new job as vice president of engineering!")
    
def playGame():
    items = []
    intro()
    floorSelection(items)

playGame()