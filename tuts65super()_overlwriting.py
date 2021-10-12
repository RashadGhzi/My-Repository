class A:
    class_var = "I am veriable in class A."
    def __init__(self):
        self.item = "I am in class A constructor."
        self.class_var = "Instance of class A."
        self.like = "Liker boy"

class B(A):
    class_var = "I am veriable of class B."
    def __init__(self):
        super().__init__()
        self.item = "I am in class B constructor."
        self.class_var = "Instance of class B."

rny = B()
print(rny.class_var)
print(rny.item)
print(rny.like)

llb = B
print(llb.class_var)

llb1 = A()
print(llb1.class_var)