#______________________Single Inheritance________________________

class student():
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def disply(self):
        print(f"Name:{self.name} \nRoll:{self.roll}")

    @classmethod
    def value(cls,item):
        return cls(*item.split("_"))


class teacher(student):
    def __init__(self,name,point,gpa):
        self.name = name
        self.point = point
        self.gpa = gpa

    def lool(self):
        print(f"Name  : {self.name} \nPoint : {self.point} \nGPA   : {self.gpa}")


ron = teacher.value("Rashad_100_2.5")
ron.lool()
