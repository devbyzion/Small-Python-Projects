import random

print ("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
Guessed_num = (int(input("Guess a number: ")))

while Guessed_num != secret_number:
    if Guessed_num > secret_number:
          print("Lower than that")

    elif Guessed_num < secret_number:
          print("Higher than that")
    Guessed_num = (int(input("Guess a number: ")))

print("Congrats! You've guessed correctly")
