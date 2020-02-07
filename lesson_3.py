# this file is to practice and take notes

# number_of_students = input("Please enter the number of students:7 ")

# print("Your name is " + number_of_students)


# while True:
#     counter = 0
#     while True:
#         counter = counter + 1
#         print("Running this code. counter:", counter)
#         if counter == 100:
#             break

# FUNCTIONS

# def fizz_buzz(input_1, input_2, text_1, text_2):
#     for i in range(input_1,input_2):
#         if (i % 3) != 0 and (i % 5) != 0:
#             print(i)
#         elif (i % 3) == 0 and (i % 5) == 0:
#             print(text_1+text_2)
#         elif (i % 3) == 0:
#             print(text_1)
#         elif (i % 5) == 0:
#             print(text_2)
        
# fizz_buzz(65, 120, "fizzes", "buzzes")

# def viveks_function(num_1, num_2, oper):
#     if oper == "+":
#         return int(num_1) + int(num_2)
#     elif oper == "-":
#         return int(num_1) - int(num_2)
#     elif oper == "*":
#         return int(num_1) * int(num_2)
#     elif oper == "/":
#         return int(num_1) / int(num_2)

# print(viveks_function(2, 2, "-"))

# def areBothEven(num_1, num_2):
#     if num_1 % 2 == 0 and num_2 % 2 == 0:
#         return True
#     else:
#         return False

# print(areBothEven(2,4))




def copy_list(list):
    my_new_list = []
    for i in list:
        my_new_list.append(i)
    return my_new_list

my_list = [1, 2, 3]
new_list = copy_list(my_list)
print(new_list)

        



