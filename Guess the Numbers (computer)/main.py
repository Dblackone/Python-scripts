
import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input("Guess a number between 1 and " + str(x) + ": "))
        if (guess == random_number):
            print("You guessed it!")
        elif (guess > random_number + 10):
            print("Your guess is too high!")
        elif (guess > random_number):
            print("Your guess is high!")
        elif (guess < random_number - 10):
            print("Your guess is too low!")
        else:
            print("Your guess is low!")

guess(30)

