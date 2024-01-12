import random
options = ["rock","paper","scissors"]
compGuess = random.choices(options)
userGuess = input("Enter rock ,  paper , scissors :")

if userGuess == "rock" and compGuess == "scissors":
    print("You Won")
if userGuess == "paper" and compGuess == "rock":
    print("You Won")
if userGuess == "scissors" and compGuess == "paper":
    print("You Won")
if userGuess == compGuess:
    print("Tie")
else :
    print(f"You lost , Computer guess was {compGuess} ")