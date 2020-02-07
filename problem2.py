angry = True
bored = True
hungry = False
tired = False

if angry and hungry and bored: 
    print("I'm angry, hungry, and bored. I will eat the Triceratops")
elif tired and hungry: 
    print("I'm tired and hungry. I will eat the Iguanadon")
elif tired: 
    print("I'm tired and will go to sleep. zzzzzzzzz")
elif angry and bored: 
    print("I'm angry and bored and I am going to fight the Velociraptor")
elif angry or bored: 
    print("Roar!")
else: 
    print("I'm doing fine! check out my smile")