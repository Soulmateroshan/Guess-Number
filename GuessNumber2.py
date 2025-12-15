import random

number=random.randint(1,10)

print("Guess the number between 1 to 10")
attempts=3 
for i in range(1,attempts+1):
    guess=int(input("Enter your guess "))

    if guess < number:
        print("to low")
    elif guess > number:
        print("to high")
    else:
        print("You Guessed it right")
        break
else:
    print(f"you have exahausted all your attempts. the number was{number}")