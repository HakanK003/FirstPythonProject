import random

ask = True

options = ["rock", "paper", "scissors"]

while ask:
    user = input("Enter Rock/Paper/Scissors ")

    random.shuffle(options)

    computer = options[0]
    #options.add(computer)
    print("Computer picked " + computer)

    if user.lower() == computer:
        print("Tie")
        continue
    if (user.lower() == "rock" and computer == "scissors") or \
            (user.lower() == "scissors" and computer == "paper") or \
            (user.lower() == "paper" and computer == "rock"):
        print("You Win")
    else:
        print("Try Again")
