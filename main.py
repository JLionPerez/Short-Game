# import difflib
import random
import sys

# global variables
choices = ["rock", "paper", "scissors"]



def playerMove():
    while True:
        choice = input("What attack do you choose? ").lower()
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
            print("There's no option for that, please try again. ", end="\n\n")


def battle():
    # playerChoice = playerMove()
    # aiChoice = random.choice(choices)
    playerPoints = 0
    aiPoints = 0

    while True:
        if playerPoints == 3:
            print("Player wins!", end="\n\n")
            break
        if aiPoints == 3:
            print("AI wins!", end="\n\n")
            break

        playerChoice = playerMove()
        aiChoice = random.choice(choices)

        print("Player chose " + playerChoice +
              " and AI chose " + aiChoice + ".")

        if playerChoice == aiChoice:
            print("It's a tie! No one gets points, keep playing!", end="\n\n")
        elif playerChoice == "rock" and aiChoice == "scissors":
            print("Player won a point!", end="\n\n")
            playerPoints += 1
        elif playerChoice == "scissors" and aiChoice == "paper":
            print("Player won a point!", end="\n\n")
            playerPoints += 1
        elif playerChoice == "paper" and aiChoice == "rock":
            print("Player won a point!", end="\n\n")
            playerPoints += 1
        else:
            print("AI won a point!", end="\n\n")
            aiPoints += 1

        # print("Player points: " + str(playerPoints) +
        #       ", AI points: " + str(aiPoints))


def main():
    print("Welcome to Rock Paper Scissors!", end="\n\n")

    # battle()

    while True:
        battle()

        answer = input("Do you want to play again? ").lower()
        if answer == "yes" or answer == "y":
            continue
        elif answer == "no" or answer == "n":
            return False
        else:
            print("There's no option for that, please try again. ", end="\n\n")

    # so the window doesn't suddenly dissappear after running
    input("Press 'Enter' to exit. ")
    sys.exit()


if __name__ == "__main__":
    main()
