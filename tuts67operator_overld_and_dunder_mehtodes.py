class luke:
    def __init__(self,name,point,marks):
        self.name = name
        self.point = point
        self.marks = marks

    #def display_value(self):
        #return f"Name:{self.name}   \nPoint:{self.point}    \nMarks:{self.marks}"

    def __add__(self, other):              # This is specia method # This is dunder method and it helps to overload add(+) operator.
        return self.point + other.marks

    def __repr__(self):
        return f"Name:{self.name}   \nPoint:{self.point}    \nMarks:{self.marks}\n"

item = luke("rashad",20,50)
item1 = luke("Harry",100,500)

#print(item.display_value())
print(item + item1)
#print(item.marks + item1.point)

print(item)
print(item1)
#print(item.display_value())