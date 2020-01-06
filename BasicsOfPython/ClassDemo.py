
class car:
    def __init__(self,make, model="i550"):
        self.make=make
        self.model=model

    def info(self):
        print("The Car make is"+self.make)
        print("The Car make is"+self.model)

class BMW(car):
    def __init__(self):
        print("This is BMW car")

