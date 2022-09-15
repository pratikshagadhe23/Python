import random
print("What is your name?")
name= input()
print("\nWelcome, " + name )

random_number= random.randint(1,20)
print("I've selected a number between 1 and 20. You have to guess that number. ")
guesses_taken =0

while guesses_taken<6:
    print("\nTake a guess")
    guess= int(input())

    guesses_taken = guesses_taken +1

    if guess > random_number:
        print("Your guess is too high. Try again")
    elif guess < random_number:
        print("Your guess is too low. Try again")
    elif guess == random_number:
        break

if guess == random_number:
    guesses_taken =str(guesses_taken)
    print("Congratulations! Your guess is right.You've taken " + guesses_taken + " attempts.")

if guess != random_number:
    random_number=str(random_number)
    print("Sorry, You lost.The number I selected was " + random_number)

