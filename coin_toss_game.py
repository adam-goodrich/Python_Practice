# Adam Goodrich Coin Toss Game
import numpy as np

# Ask for player names
p1_name = input("What is the name of player 1? ")
p2_name = input("What is the name of player 2? ")

# explaingin the game
print("\nWe will flip a coin until we get heads 50 times.")
print("How many flips will it take? The player who guesses closest to the correct number wins!\n")

# asking for the user input using a while loop to check for valid input
play_again = "y"

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
            return ("\n" + "Wow! It was a tie! There were " + str(heads + tails) + " flips.\n")
        # this will print if player 1 wins
        elif abs((heads + tails) - int(p1_guess)) < abs((heads + tails) - int(p2_guess)):
            return ("\n" + p1_name.upper() + " WON! There were " + str(heads + tails) + " flips.\n")
        # this will print if player 2 wins
        else:
            return ("\n" + p2_name.upper() + " WON! There were " + str(heads + tails) + " flips.\n")
    
    # calling the function and declaring the winner
    print(coin_game(p1_guess, p2_guess))
    # getting input to see if they want to play again
    play_again = input("Do you want to play again? (y)es or (n)o: \n")
    play_again = play_again.lower()
# GAME OVER when they break the loop
print("\nThanks for playing!\n")