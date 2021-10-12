class like():
    def __init__(self, aname, aroll, amarks):
        self.name = aname
        self.roll = aroll
        self.marks = amarks

    def display(self):
        print(f"Name:{self.name} \nRoll:{self.roll} \nMarks:{self.marks}")

    @classmethod
    def value(cls,item):
        return cls(*item.split("_"))

    @staticmethod           # No need to use (self) and (cls). Any object can access this function
    def good(string):
        print(string+" is a good boy.")

harry = like.value("Harry_50_100")
harry.display()
harry.good("Harry")

like.good("Rony")

