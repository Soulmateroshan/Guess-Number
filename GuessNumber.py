import random

number=random.randint(1,100)

print("Guess the number between 1 to 100")
attempts = 0
while True:
    guess=int(input("Enter your guess number"))

    attempts+=1

    if guess < number:
        print("to low")
    elif guess > number:
        print("to high")
    else:
        print("You Guessed it right, You took =",attempts,"attempts")
        break