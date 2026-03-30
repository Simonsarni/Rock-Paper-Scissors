import random


def RockPaperScissors():
    user_choice = input("Enter your choice: Rock / Paper / Scissors: ").lower()
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    print(f"You chose {user_choice} and the computer chose {computer_choice}")

    if computer_choice == user_choice:
        print("You tie, try again")
        RockPaperScissors()
    elif computer_choice == "rock":
        if user_choice == "paper":
            print("Paper cover Rock, you win! :)")
        elif user_choice == "scissors":
            print("Rock smash the Scissors, you lose :(")
    elif computer_choice == "paper":
        if user_choice == "scissors":
            print("Scissors cut paper, you win! :)")
        elif user_choice == "rock":
            print("Paper cover Rock, you lose :(")
    elif computer_choice == "scissors":
        if user_choice == "rock":
            print("Rock smash the Scissors, you win! :)")
        elif user_choice == "paper":
            print("Scissors cut Paper, you lose :(")


RockPaperScissors()
