#________________________Multilevel Inheritance___________________________#
class A:
    a = 10
    def print_display_1(self):
        return f"This is {self.a}"

class B(A):
    b = 20
    def print_display_2(self):
        return f"This is {self.b}"

class C(B):
    c = 30
    def print_display_3(self):
        return f"This is {self.c}"

harry = C()
print(harry.print_display_1())
print(harry.print_display_2())
print(harry.print_display_3())