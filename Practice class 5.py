# this file is to practice and take notes
import os
os.system("clear")
# Multiple arguments in a function

# def combine_strings(*my_list):
#     s = ""
#     for i in my_list:
#         s += i
#     s = (" ".join(s))
#     return s

# print(combine_strings("Hi", "How", "are", "you"))

# def sum_everything(*nums):
#     start_num = 0
#     for i in nums:
#         start_num += i
#     return start_num

# print(sum_everything(4, 5, 6))

# def yogurt_land(spoon, **kwargs):
#   print(spoon)
#   # We need a loop, because we don't know how many kwargs there are.
#   for keyword, flavor in kwargs.items():
#     # kwargs.items has the keyword and the value, which we're calling "flavor" in the loop.
#     print(keyword)
#     print(flavor)
#     # print("My", keyword, "is a", flavor)
# # Like before, the unnamed arg has to come first!
# yogurt_land("large!", first_froyo="vanilla", second_froyo="chocolate", third_froyo="banana")

# def first_last(**first_last_names):
#     for first, last in first_last_names.items():
#         print(first, last)
#     return ""

# print("This", "is", "a", "sentance", sep="\u263A")
# def greater_than(*x):
#     counter = 0
#     for num in x:
#         if num > 50:
#             counter += 1
#     return counter

# print(greater_than(1, 60, 100, 500))
# print_address(first_name="john", last_name="Doe", city="Boston", zip_code="02100")
# def print_address(**address_info):
#     for input_1, input_2 in address_info.items():
#         if "first_name" in address_info:
#             print(input_2)
        
#     return ""

# print(print_address(first_name="john", last_name="Doe", city="Boston", zip_code="02100"))

# {"puppy":"Small dog",
# "cat":"great pet"}

# thisdict = {
#     "brand":"Ford",
#     "Model":"Mustang",
#     "Year":1964
# }
# for key, value in thisdict.items():
#     print("The", key, "is", value, end=", ")
# # print(thisdict)

# my_name = {
#     "A":2,
#     "D":1,
#     "M":1
# }

# for key, value in my_name.items():
#     print("The letter", key, "is in my name", value, "times.")


# def check_if_in_class(*members):
#     pyt_class = ["Chuck", "Tim", "eva", "Matt", "Adam"]
#     for person in members:
#         if person in pyt_class:
#             print(person + " True")
#         else:
#             print(person + " False")
#     return ""
    
# print(check_if_in_class("Chuck", "Vivek", "Nadia", "Adam"))


# def print_address(**kw_info):
#     if "street" in kw_info:
#         print(kw_info["first_name"], kw_info["last_name"])
#         print(kw_info["street"])
#         print(kw_info["city"], kw_info["zip_code"])
#         return ""
#     else:
#         print(kw_info["first_name"], kw_info["last_name"])
#         print(kw_info["city"], kw_info["zip_code"])
#         return ""

# print(print_address(first_name="John", last_name="Doe", city="Boston", zip_code="02100"))

# def Name_dictonary(name):
#     new_dict = {} 
#     name = name.upper()
#     for i in name: 
#         if i in new_dict: 
#             new_dict[i] += 1
#         else: 
#             new_dict[i] = 1
#     return (new_dict)

# print(Name_dictonary("John Doe"))


# my_dictonary = {
#     "dog": "cute, furry animal",
#     "cat": "cute, arrogant animal",
#     "elephant": "large mammal"}

# print(my_dictonary.items())

# for k, v in my_dictonary.items():
#     print(k, v, sep=" : ")

words = {
    "hello",
    "water",
    "hello",
    "hello",
}

# def most_popular_words(words):
#     names = {}
#     for i in words:
#         if i in names: 
#             names[i] += 1
#         else:
#             names[i] = 1
#     return names
        
# print(most_popular_words(words))
#  
# state_capitals = {
#   "Alaska" : "Juneau",
#   "Colorado" : "Denver",
#   "Oregon" : "Salem",
#   "Texas" : "Austin"
#   }

# def reverse_lookup(dict):        
#     which_city = input("what city? ")
#     for k, v in state_capitals.items():
#         if v == which_city:
#             return (k + " is the state " + which_city + " is in.")
            

# print(reverse_lookup(state_capitals))

# sets and tuples

# my_list = ["yellow", "red", "green", "yellow"]
# print(my_list)
# my_set = set(my_list)

# new_list = list(my_set)
# print(new_list)

# clothing_list = ["blue", "grey", "brown", "blue", "green"]

# clothing_set = set(clothing_list)

# for i in clothing_list, clothing_set:
#     new_list = []
#     if i in clothing_list:
#         new_list += i
#         print(new_list[0])
#     else:
#         print(i)

# first_tuple = (1, 45, 67)

# print(first_tuple[1])

# for i in first_tuple:
#     print(i)

# seasons = ("Fall", "Winter", "Spring", "Summer")

# for i in seasons:
#     print(i)

# the_type = type(seasons)
# print(the_type)

foods_list = ["coffee", "burgers"]

foods_set = {"coffee", "burgers"}

foods_tuple = ("coffee", "burgers")

food_set_2 = set(foods_list)

foods_list.append("pizza")
foods_list.append("eggs")

foods_set.add("pizza")
foods_set.add("eggs")

food_set_2.add("pizza")
food_set_2.add("eggs")

print("\nFirst list")
print(foods_list)
print(foods_set)
print(foods_tuple)
print(food_set_2)


foods_list.remove("pizza")
foods_set.remove("pizza")
food_set_2.remove("pizza")

print("\nSecond list")
print(foods_list)
print(foods_set)
print(foods_tuple)
print(food_set_2)

foods_list.pop[1]
foods_list.inset("popcorn")[1]
# foods_set.remove("pizza")
# food_set_2.remove("pizza")

print(foods_list)
print(foods_set)
print(foods_tuple)
print(food_set_2)




