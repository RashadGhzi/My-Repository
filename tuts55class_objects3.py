class item():
    def __init__(self,name,roll,point):
        self.name = name
        self.roll = roll
        self.point = point
    def display(self):
        print(f"Name:{self.name}, Roll:{self.roll}, Point:{self.point}")

liek = item("Rashad", 20,50)
liek.display()