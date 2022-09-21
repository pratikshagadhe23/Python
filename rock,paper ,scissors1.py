import random
choices = ["rock","paper","scissors"]
computer= random.choice(choices)

player = None

while player not in choices:
    player = input("rock,paper or scissors : ").lower()


def game ():
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie")
        return()

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            return()
        
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            return() 
    
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            return()
            
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            return()

    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            return()
        
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            return()

game()