import random

go_again = "y"


player_score_count = 0
computer_score_count = 0
while go_again == "y":
    your_choice = input("\nPlease chose either Rock, Paper, or Sissors: ")
    rock_paper_sissor = random.choice(["Rock", "Paper", "Sissors"])
    
    print(f"\nYou picked {your_choice}.")
    print(f"\nThe Computer picked {rock_paper_sissor}.")

    your_choice = your_choice.lower()
    rock_paper_sissor = rock_paper_sissor.lower()


    if your_choice == rock_paper_sissor:
        print("\nIt was a tie!")
    elif your_choice == "rock" and rock_paper_sissor == "paper":
        print("\nYou lose!")
        computer_score_count += 1
    elif your_choice == "rock" and rock_paper_sissor == "sissors":
        print("\nYou win!")
        player_score_count += 1
    elif your_choice == "paper" and rock_paper_sissor == "sissors":
        print("\nYou lose!")
        computer_score_count += 1
    elif your_choice == "paper" and rock_paper_sissor == "rock":
        print("\nYou win!")
        player_score_count += 1
    elif your_choice == "sissors" and rock_paper_sissor == "rock":
        print("\nYou lose!")
        computer_score_count += 1
    elif your_choice == "sissors" and rock_paper_sissor == "paper":
        print("\nYou win!")
        player_score_count += 1
    else:
        print("\nSorry I don't understand. Please only pick 'Rock', 'Paper', or 'Sissors'.")


    print(f"\nThe current score is computer {computer_score_count}, you {player_score_count}.")
    go_again = input("\ngo again? ")
    go_again = go_again.lower()
