# numbers you want to find the common multiples of x is lower number y is higher number
x = 1350
y = 2100
# varibles for what multiples you are looking for
a = 10
b = 5
# for loop to find common multiples up t
for num in range(x,(y+1)):
    if not(num % a) and not(num % b):
        print(num)