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
        if playerPoints == 3:
            print("Player wins!")
            break
        if aiPoints == 3:
            print("AI wins!")
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
    battle()
    # x = playerMove()
    # print("Player chose: ", x)


if __name__ == "__main__":
    main()
