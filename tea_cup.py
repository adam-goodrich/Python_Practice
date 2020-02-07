
class tea_cup:
    def __init__(self, capacity=3, amount="Empty"):
        self.capacity = capacity
        self.amount = amount

    def fill(self):
        if self.amount == "Empty":
            print(f"I need to fill up my cup! it can hold {self.capacity} pours")
        if self.amount == "Half Full":
            print(f"My cup is {self.amount}. it can hold {self.capacity-1} pours")
        if self.amount == "Almost Full":
            print(f"My cup is {self.amount}. it can hold {self.capacity-2} pours")
        if self.amount == "Full":
            print(f"My cup is {self.amount}. it can not hold any more pours")

    def empty(self):


    def drink(self):

cup1 = tea_cup(amount="Half Full")

cup1.fill()
