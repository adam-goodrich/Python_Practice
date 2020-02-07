temperature = 90

while temperature > 75:
    print(f"Temperature is {temperature} - crank the AC!")
    temperature = temperature - 3
    while temperature < 75:
        temperature = temperature + 1

print("75. Ahh, that's better.")