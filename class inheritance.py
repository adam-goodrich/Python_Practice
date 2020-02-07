# Class Notes
# Inheritance
# 

class animals:

    def __init__(self, weight=1, height=1):
        self.weight = weight
        self.height = height

    def breathe(self):
        print(f"I am breathing because I am {self.weight} weight and {self.height} height")

    def sound(self):
        print(f"I make sounds because I am {self.weight} weight and {self.height} height")





class dog(animals):
    def __init__(self, name="", weight=0, height=0):
        super().__init__(weight, height)
        self.name = name

    def sound(self):
        print(f"woof woof!! My name is {self.name}")
        print(f"I am a Dog. I make sounds because I am {self.weight} weight and {self.height} height")

class cat(animals):
    def __init__(self, name="", weight=0, height=0):
        super().__init__(weight, height)
        self.name = name

    def sound(self):
        print(f"Meow!! My name is {self.name}")
        print("I am a Cat. I think I am better than any Dog")
        print(f"I make sounds because I am {self.weight} weight and {self.height} height")

mouse = animals(2, 4)

mouse.breathe()

puppy = dog("Abbie", 6, 8)

puppy.sound()

kitty = cat("Beans", 2, 3)

kitty.sound()
