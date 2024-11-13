# Guess the number 
import random

guess = -1
number = random.randiant(0,101)

while guess != number: 

    try: 
     guess = input("Whats your guess?\n>")

    if guess > number:
        print("Too small, try again...")

    elif guess > number:
        print()"Too small, try again...)   

    else: 
        print("Bingo! The correct number wwas " + str(number))