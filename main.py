# import difflib
import random


# global variables
choices = ["rock", "paper", "scissors"]


def playerMove():
    while True:
        choice = input("What attack do you choose? ")
        # choice = difflib.get_close_matches(choice, choices)
        # print(choice)

        if choice == "rock":
            # print("rock")
            return "rock"
        elif choice == "paper":
            return "paper"
        elif choice == "scissors":
            return "scissors"
        else:
            print("There's no option for that, please try again. ")


def battle():
    # playerChoice = playerMove()
    # aiChoice = random.choice(choices)
    playerPoints = 0
    aiPoints = 0
    
    while True:
        # if playerPoints == 3:
        #     print("Player wins!")
        # if aiPoints == 3:
        #     print("AI wins!")
        playerChoice = playerMove()
        aiChoice = random.choice(choices)

        if playerChoice == aiChoice:
            print("It's a tie! No one gets points, keep playing!")
        elif playerChoice == "rock" and aiChoice == "scissors":
            playerPoints += 1
        elif playerChoice == "scissors" and aiChoice == "paper":
            playerPoints += 1
        elif playerChoice == "paper" and aiChoice == "rock":
            playerPoints += 1
        else:
            aiPoints += 1


def main():
    battle()
    # x = playerMove()
    # print("Player chose: ", x)


if __name__ == "__main__":
    main()
