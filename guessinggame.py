import random

number_to_guess = random.randint(1, 10)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < (7):
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")

print("Congratulations! You guessed the number.")