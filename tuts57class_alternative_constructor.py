class student():
    def __init__(self,aname,aroll,amarks):
        self.name = aname
        self.roll = aroll
        self.marks = amarks

    def display(self):
        print(f"Name:{self.name} \nRoll:{self.roll} \nMarks:{self.marks}")

    @classmethod
    def value_pass(cls,string):
        #string1 = string.split("-")
        #eturn cls(string1[0],string1[1],string1[2])
        return cls(*string.split("-"))

Rakib = student.value_pass("Rashad-50-100")
Rakib.display()