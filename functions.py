# from didyoumean3.didyoumean import did_you_mean

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Enemy:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type # monster type
        self.health = health



# options in battle, will also be used to determine who goes first; might not be needed
def battle_options(option):
    name = ""
    choice = option.lower()

    if choice == "rock":
        name = "rock"
    elif choice == "paper":
        name = "paper"
    elif choice == "scissor" or choice == "scissors":
         name = "scissor"
    else:
        return "Please choose either rock, paper, or scissor."
    return name

# determines who wins rock paper and scissors; 
def who_goes_first(Player, player_choice, Enemy, enemy_choice):
    p = Player.name
    e = Enemy.name

    # rock beats scissor
    if player_choice == "rock" and enemy_choice == "scissor":
        return p
    elif enemy_choice == "rock" and player_choice == "scissor":
        return e
    # scissor beats paper
    elif player_choice == "scissor" and enemy_choice == "paper":
        return p
    elif enemy_choice == "scissor" and player_choice == "paper":
        return e
    # paper beats rock
    elif player_choice == "paper" and enemy_choice == "rock":
        return p
    elif enemy_choice == "paper" and player_choice == "rock":
        return e
    # if they're the same send out 1, will trigger to ask player again
    return 1



# enemies description
# werewolves - very strong attacks; favors rock
# witches - poison; long conditions; favors paper
# cat people - quick attackers can attack several times in one turn; boss has 9 lives; favors scissors
# mermaids - constant healing of themselves; favors paper and scissor

p = Player("Joggo", 100)
e = Enemy("Selene", "Mermaid", 100)

# print(p.name)
# print(e.name)

# print(battle_options("pa"), end='')

def loopy_func(Player, player_choice, Enemy, enemy_choice):
    name = ""
    while True:
        print("Rock, paper, scissor...Shoot!")
        # have to make a function that asks the player what their choice is
        if who_goes_first(Player, player_choice, Enemy, enemy_choice) != 1:
            name = who_goes_first(Player, player_choice, Enemy, enemy_choice)
            return name
        print("It's a tie, keep playing!")


print(loopy_func(p, "rock", e, "rock"))