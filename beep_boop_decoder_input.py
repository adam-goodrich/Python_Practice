letters = [
    ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z']
phrase = []
more_input = "y"
while more_input == "y":
    beeps = int(input("How many beeps? "))
    boops = int(input("How many boops? "))
    more_input = input("Is there another input? y/n: ")
    if beeps >= 0 and boops >= 0 and more_input == "y":
        total = int(beeps) + int(boops)
        letter = letters[total]
        phrase.append(letter)
        more_input = more_input.lower()
    elif more_input == "n":
        break
    else:
        print("I don't understand, try again")

print("".join(phrase))
