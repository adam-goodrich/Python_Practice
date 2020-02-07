my_num = input("Please give me a number: ")

try:
    print(my_num)
except ValueError as e:
    print("That is not a number")



