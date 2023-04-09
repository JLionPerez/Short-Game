# import difflib

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


def main():
    x = playerMove()
    print("Player chose: ", x)


if __name__ == "__main__":
    main()
