# rock, paper, scissors game
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

if player == computer:
    print("Draw!")
    print("computer: ", computer)
    print("player: ", player)

elif player == "rock":
    if computer == "paper":
        print("You lose!")
        print("computer: ", computer)
        print("player: ", player)
    elif computer == "scissors":
        print("You win!")
        print("computer: ", computer)
        print("player: ", player)
elif player == "paper":
    if computer == "rock":
        print("You win!")
        print("computer: ", computer)
        print("player: ", player)
    elif computer == "scissors":
        print("You lose!")
        print("computer: ", computer)
        print("player: ", player)
else:
    if computer == "rock":
        print("You lose!")
        print("computer: ", computer)
        print("player: ", player)
    elif computer == "paper":
        print("You win!")
        print("computer: ", computer)
        print("player: ", player)
