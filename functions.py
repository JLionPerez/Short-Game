# from didyoumean3.didyoumean import did_you_mean

class Player:
    def __init__(self, name, health, choice):
        self.name = name
        self.health = health
        self.choice = choice

class Enemy:
    def __init__(self, name, type, health, choice):
        self.name = name
        self.type = type # monster type
        self.health = health
        self.choice = choice



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
def who_goes_first(Player, Enemy):
    p = Player
    e = Enemy

    # rock beats scissor
    if Player.choice == "rock" and Enemy.choice == "scissor":
        return p
    elif Enemy.choice == "rock" and Player.choice == "scissor":
        return e
    # scissor beats paper
    elif Player.choice == "scissor" and Enemy.choice == "paper":
        return p
    elif Enemy.choice == "scissor" and Player.choice == "paper":
        return e
    # paper beats rock
    elif Player.choice == "paper" and Enemy.choice == "rock":
        return p
    elif Enemy.choice == "paper" and Player.choice == "rock":
        return e
    # if they're the same send out 1, will trigger to ask player again
    return 1



# enemies description
# werewolves - very strong attacks; favors rock
# witches - poison; long conditions; favors paper
# cat people - quick attackers can attack several times in one turn; boss has 9 lives; favors scissors
# mermaids - constant healing of themselves; favors paper and scissor

p = Player("Joggo", 100, "rock")
e = Enemy("Selene", "Mermaid", 100, "scissor")

# print(p.name)
# print(e.name)

# print(battle_options("pa"), end='')

def loopy_func(Player, Enemy):
    first_player = 0 # it takes in an int, but need to take in Player or Enemy object
    second_player = 0
    while True:
        print("Rock, paper, scissor...Shoot!")
        # have to make a function that asks the player what their choice is
        if who_goes_first(Player, Enemy) != 1:
            first_player = who_goes_first(Player, Enemy)
            # return first_name
            print(first_player.name + " threw " + first_player.choice)
            print(second_player.name + " threw " + second_player.choice)
        print("It's a tie, keep playing!")


loopy_func(p, e)