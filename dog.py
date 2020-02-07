class Dog:
    
    total_dogs = 0

    def __init__(self, breed="", color="black", size=5, mood="happy", **kwargs):
        Dog.total_dogs += 1
        self.breed = breed
        self.color = color
        self.size = size
        self.mood = mood
        

    def bark(self):
        print(f"Woof woof. My color is {self.color}")

    def sit(self):
        print(f"I am now sitting. I am a good {self.breed} boi")

    def run(self):
        if self.mood == "angry":
            print(f"When I am running I am {self.mood} {self.breed}")
        else:
            print(f"I love running. Being a {self.breed} is fun!!!")

    def eat(self):
        print(f"I am eating and I am {self.size} pounds")

dog1 = Dog(breed="lab", color="white", size=10,)

dog2 = Dog(breed="Pit Bull", mood="angry")

dog1.run()
dog1.sit()
dog1.bark()
dog1.eat()

print("\n")

dog2.run()
dog2.sit()
dog2.bark()
dog2.eat()

print(Dog.total_dogs)
    

