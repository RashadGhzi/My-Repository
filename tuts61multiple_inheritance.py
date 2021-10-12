#__________________________Multiple Inheritance__________________________#
class employee:
    def __init__(self,name,point):
        self.name = name
        self.point = point

    def display_value(self):
        return f"Name  : {self.name} \nPoint  : {self.point}"
    @classmethod
    def valuer_take(cls,item):
        return cls(*item.split("_"))


class player:
    def __init__(self,name,game,like):
        self.name = name
        self.game = game
        self.like = like

    def display_value1(self):
        return f"Name  : {self.name} \nGame  : {self.game} \nLike:{self.like}"

    @classmethod
    def valuer_take1(cls, item):
        return cls(*item.split("_"))


class programmer(employee,player):
    text = "Good boy"
    def text_print(self):
        print(self.text)


harry = programmer.valuer_take("Harry_100")
print(harry.display_value())
harry.text_print()

