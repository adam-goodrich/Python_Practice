# Adam Goodrich Coin Toss Game
import numpy as np
# Ask for player names
p1_name = input("What is the name of player 1? ")
p2_name = input("What is the name of player 2? ")
# explaingin the game
print("\nWe will flip a coin until we get heads 50 times. How many flips will it take? closest to the number wins!\n")

p1_guess = input(p1_name + ", how many flips will it take to get to 50 heads? ")
p2_guess = input(p2_name + ", how many flips will it take to get to 50 heads? ")


def coin_game(p1_guess,p2_guess):
    heads = 0
    tails = 0
    while heads < 50:
        toss = np.random.random() > 0.5
        if toss:
            heads += 1
        else:
            tails += 1
    if abs((heads + tails) - int(p1_guess)) < abs((heads + tails) - int(p2_guess)):
        return (p1_name + " WON! There were " + str(heads + tails) + " flips.")
    else:
        return (p2_name + " WON! There were " + str(heads + tails) + " flips.")

print(coin_game(p1_guess, p2_guess))