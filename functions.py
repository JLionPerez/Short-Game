# from didyoumean3.didyoumean import did_you_mean

def player_options(option):
    name = ""
    if option == "rock":
        name = "rock"
    elif option == "paper":
        name = "scissors"
    elif option == "scissor" or "scissors":
        name = "scissor"
    return name

print(player_options("scissors"), end='')