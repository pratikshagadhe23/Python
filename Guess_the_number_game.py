import random

number = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50 : "))

while guess!=number:
    if guess> number:
        print("Guess a lower number. Try again")
        guess = int(input("\nGuess a number between 1 and 50 : "))
    else:
        print("Guess a higher number. Try again")
        guess = int(input("\nGuess a number between 1 and 50 : "))
        
print("Congratulations, You won! You guessed the right number.")
