import random
user_name = input("Enter your name: ")
print("\nWelcome to the guessing game "+ user_name)

def game():
    random_number = random.randrange(1,100)
    print("\nI've selected a number between 1 and 100")
    print("You've 6 chances to guess that number. Good luck!")
    i=1
    r=1
    while i<7:
        user_number= int(input("Enter a number : "))
        if user_number < random_number:
            print("\n" + user_name + " My number is greater than your number. Try again")
            print("You've " + str(6-i) + "chances left.")
            i=i+1
        elif user_number > random_number:
            print("\n" + user_name + " My number is smaller than your number. Try again")
            print("You've " + str(6-i) + "chances left.")
            i=i+1
        elif user_number == random_number:
            print("\nCongratulations!" + user_name + "You guessed the correct number.")
            r=0
            break
    if r==1:
            print("Sorry you lost the game")
            print("My number was : " + str(random_number))
def main():
    game()
    while True:
        another_game = input("Do you wish to play again? (y/n): ")
        if another_game =="y":
            game()
        else:
            break
main()
print("\nEnd of the game! Thank you for playing.")