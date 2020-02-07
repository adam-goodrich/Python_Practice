# Adam Goodrich Coin Toss Game
import numpy as np
import os
os.system("clear")

# coin toss game function and returning the winner
def coin_game(p1_guess,p2_guess):
    # this is the coin toss, it repeats until 50 heads
    heads = 0
    tails = 0
    while heads < 50:
        toss = np.random.random() > 0.5
        if toss:
            heads += 1
        else:
            tails += 1
    # This will print just in case there is a tie
    if abs((heads + tails) - int(p1_guess)) == abs((heads + tails) - int(p2_guess)):
        return ("Wow! It was a tie! There were " + str(heads + tails) + " flips.\n")
    # this will print if player 1 wins
    elif abs((heads + tails) - int(p1_guess)) < abs((heads + tails) - int(p2_guess)):
        return ("Cool, " + p1_name.upper() + " WON! There were " + str(heads + tails) + " flips.\n")
    # this will print if player 2 wins
    else:
        return ("Aweseome, " + p2_name.upper() + " WON! There were " + str(heads + tails) + " flips.\n")

# Ask for player names
p1_name = input("What is the name of player 1? ")
p2_name = input("What is the name of player 2? ")

def full_game(p1_name, p2_name):
    # explaingin the game
    print("\nWe will flip a coin until we get heads 50 times.")
    print("How many flips will it take? The player who guesses closest to the correct number wins!\n")

    # asking for the user input using a while loop to check for valid input
    play_again = "y"
    tie_counter = 0
    p1_counter = 0
    p2_counter = 0
    while play_again == "yes" or play_again == "y":
        p1_guess = 1
        p2_guess = 1
        while p1_guess == p2_guess:
            p1_guess = input("\n" + p1_name + ", guess how many flips will it take to get to 50 heads? ")
            p2_guess = input("\n" + p2_name + ", guess how many flips will it take to get to 50 heads? ")
            # this if statement checks if users both put same number, if so they must guess again
            if p1_guess == p2_guess:
                print("\nGuesses can not be the same number. Both players must guess again.\n")
            # this try/except checks if the input is a interger. only intergers will be accepted or else they must guess again
            try:
                p1_guess = int(p1_guess)
                p2_guess = int(p2_guess)
            except ValueError:
                p1_guess = 1
                p2_guess = 1
                print("\nBoth guesses must be an integer. Both players must guess again.\n")
        
        # calling the function and declaring the winner
        counter = coin_game(p1_guess, p2_guess)
        print(counter)
        # This is a score counter
        if counter[0] == "W":
            tie_counter += 1
        elif counter[0] == "C":
            p1_counter += 1
        elif counter[0] == "A":
            p2_counter += 1
        print("The score so far...")
        print(p1_name + " Won " + str(p1_counter) + ".")
        print(p2_name + " Won " + str(p2_counter) + ".")
        print("There are " + str(tie_counter) + " ties.")
        # getting input to see if they want to play again
        play_again = input("Do you want to play again? (y)es or (n)o: \n")
        play_again = play_again.lower()
    # GAME OVER when they break the loop
    print("\nThanks for playing!\n")
full_game(p1_name, p2_name)


