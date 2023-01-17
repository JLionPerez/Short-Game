import random

# basic AI rock paper scissors
def opponent_ai():
    #different chances
    chance = random.choice([1,2,3])
    #rock
    if chance == 1:
        print("rock")
    #paper
    if chance == 2:
        print("paper")
    #scissors
    if chance == 3:
        print("scissors")

# for x in range(100):
#     opponent_ai()

def game():
    # if player