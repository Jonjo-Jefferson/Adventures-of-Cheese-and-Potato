##### Adventures of Cheese and Potato #####
##### 24-2-24 #####
# print("hello adventurer and welcome to the dungeon of cheese and potatos!")
# print("before you can enter the dungeon I must know your age")
# age = input()
# if (int(age)) <= 20:
#     print("Fuck off you underaged twat")
# if (int(age)) >= 20:
#     print("Yippie, you are old enough to enter the dungeon!")
import time


def babySausage():
    print("You walk through the dark and slowly hear...... a baby??")
    time.sleep(1)
    print("You see a sausage baby sitting in the middle of the room")
    time.sleep(2)
    print("What do you do??? - Options: left - l | Right = r | Forward = f | eat = a")
    userInput = input()
    if userInput == "a":
        time.sleep(1)
        print("You eat the sausage baby")
        time.sleep(1)
        print("The sausage baby is a bit of sausage and pastry, but it's not too bad")
        time.sleep(2)
        print("You then hear a sausage roll titan coming from underground!!!!!")
        time.sleep(3)
        print(
            "What do you do?!?!? Options: left - l | Right = r | Forward = f | Action = a"
        )
        actionInput = input()
        if actionInput == "l":
            print(
                "You run head first into a wall. And the sausage roll monster, eats you alive"
            )
        if actionInput == "r":
            print(
                "You run into the sausage babys mum. She asks for 25 schmeckles. But you don't have"
            )
            print("25 schmeckles!! So the sausage babys mum bites your head of")


def discoveryOne():
    directions = ["l", "r", "f", "a"]
    print("You enter a room covered in bits of sausage and pastry")
    userInput = ""
    actionInput = ""
    while userInput not in directions:
        print("Options: left - l | Right = r | Forward = f | Action = a")
        userInput = input()
        if userInput == "a":
            print("You walk closer to the remains only to discover...")
            print(
                "Its a trap! There are angry sausage roll monsters on the roof ready to jump down and nibble on your toes"
            )
            print("Do you chose to run or attack?")
            print("Options: run | attack")

            actionInput = input()
            if actionInput == "run":
                print(
                    "you try to run, but then you realise that these sausage rolls are trained athletic runners"
                )
                print(
                    "they catch up to you in the blink of an eye and start nibbling your toes!"
                )
            elif actionInput == "attack":
                print(
                    "You try to punch the sausage roll, but you quickly find out they are trained in martial arts!"
                )
                print(
                    "The sausage roll ducks out of the way, swings his sausage arms, and snaps your jaw!"
                )
                print("And then proceeds to nibble on your toes!")
                print("YOU DIED")
        elif userInput == "l":
            time.sleep(0.5)
            babySausage()


def crossroads():
    directions = ["left", "right", "forward"]
    print(
        "You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?"
    )
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward/action")
        userInput = input()
        if userInput == "l":
            showShadowFigure()
        elif userInput == "r":
            showSkeletons()
        else:
            print("Please enter a valid option for the adventure game.")


if __name__ == "__main__":
    while True:
        print("Welcome to the Adventure Game!")
        print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " + name + ".")
        discoveryOne()
