def main():
        print("Welcome to the Adventure Game!")
        print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration , you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name. ")
        name= input()
        print("Good luck, " + name+ ".")
        introscene()   
            
def introscene():
    directions= ["left","right","forward","backward"]
    print("You are at a crosswords, and you can choose to go down any of the four hallways. Where would you like to go?")
    user_input= ""
    while user_input not in directions:
        print("Options: left/right/forward/backward")
        user_input= input()
        if user_input == "left":
            ShowShadowFigure()
        if user_input == "right":
            ShowSkeletons()
        if user_input == "forward":
            HauntedRoom()
        if user_input == "backward":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")


def ShowShadowFigure():
    directions = ["right","left","backward"]
    print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    user_input= ""
    while user_input not in directions:
        print("Options: right/left/backward")
        user_input= input()
        if user_input == "right":
            CameraScene()
        if user_input == "left":
            print("You find that this door opens into a wall.")
        if user_input == "backward":
            introscene()
        else:
            print("Please enter a valid option.")

def CameraScene():
    directions = ["forward","backward"]
    print("You see a camera that has been dropped on the ground.Someone has been here recently. Where would you like to go?")
    user_input= ""
    while user_input not in directions:
        print("Options: forward/backward")
        user_input= input()
        if user_input == "forward":
            print("You made it!You've found an exit.")
            quit()
        if user_input == "backward":
            ShowShadowFigure()
        else:
            print("Please enter a valid option.")

def HauntedRoom():
    directions = ["right","left","backward"]
    print("You hear strange voices.You think you have awoken some of the dead.Where would you like to go?")
    user_input= ""
    while user_input not in directions:
        print("Options: right/left/backward")
        user_input= input()
        if user_input == "right":
            print("Multiple ghoul -like creatures start emerging as you enter the room. You are killed.")
            quit()
        elif user_input == "left":
            print("You made it! You've found an exit.")
            quit()
        elif user_input == "backward":
            introscene()
        else:
            print("Please enter a valid option.")

weapon =False

def ShowSkeletons():
    directions = ["backward","forward"]
    global weapon
    print("You see a wall of skeletons as you walk into the room.Someone is watching you.Where would you like to go?")
    user_input= ""
    while user_input not in directions:
        print("Options: left/backward/forward")
        user_input= input()
        if user_input == "left":
            print("You find that this door opens into a wall.You open some of the drywall to discover a knife.")
            weapon = True
        elif user_input == "backward":
            introscene()
        elif user_input == "forward":
            StrangeCreature()
        else:
            print("Please enter a valid option.")

def StrangeCreature():
    actions = ["right","flee"]
    global weapon
    print("A strange creature has appeared. You can either run or fight it.What would you like to go?")
    user_input= ""
    while user_input not in actions:
        print("Options: flee/fight")
        user_input= input()
        if user_input == "fight":
            if weapon:
                print("You kill the creature with the knife you found earlier. After moving forward, you find one of the exits.Congrats!")
            else:
                print("The craeture has killed you.")
            quit()
        elif user_input == "flee":
            ShowSkeletons()
        else:
            print("Please enter a valid option.")


main()

