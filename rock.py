import random
go_again = "y"
while go_again == "y":
    rock_paper_sissor_1 = random.choice(["Rock", "Paper", "Sissor"])
    rock_paper_sissor_2 = random.choice(["Rock", "Paper", "Sissor"])
    print("Outsider is ", rock_paper_sissor_1)
    print("Space show is ", rock_paper_sissor_2)
    
    go_again = input("go again? ")
