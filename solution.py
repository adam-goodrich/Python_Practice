import os
os.system("clear")

sports = {
    "Tennis": 2,
    "Soccer": 22,
    "Volleyball": 4,
    "Baseball": 50
}
tab = ""
for k, v in sports.items():
    print(f"{tab}I like \"{k}\" \n{tab}There are usually {v} players in \"{k}\"")
    tab += "\t"
    

    