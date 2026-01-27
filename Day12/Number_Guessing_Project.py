import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
choice=input("Choose a mode- easy(10 tries) /hard (5 tries):")
print("I have thought of a random number between 1 and 100.")
print("Can you guess it?")
number=random.randint(1,100)
if choice=="easy":
    lives=10
    while lives>0:
        guess=int(input("Guess the number: "))
        if guess==number:
            print("You got it! The number is " + str(number)+"!")
            break
        elif guess>number:
            print("You guessed too high!")
            lives-=1
            print(f"You have {lives} guesses left")

        elif guess<number:
            print("You guessed too low!")
            lives-=1
            print(f"You have {lives} guesses left")

elif choice=="hard":
    lives = 5
    while lives > 0:
        guess = int(input("Guess the number: "))
        if guess == number:
            print("You got it! The number is " + str(number) + "!")
            break
        elif guess > number:
            print("You guessed too high!")
            lives-=1
            print(f"You have {lives} guesses left")

        elif guess < number:
            print("You guessed too low!")
            lives-=1
            print(f"You have {lives} guesses left")














