class A:
    def meth(self):
        print("I am in class A method.")
class B(A):
    #def meth(self):
        #print("I am in class B method.")
        pass
class C(A):
    #def meth(self):
        #print("I am in class C method.")
    pass
class D(B,C):
    #def meth(self):
        #print("I am in class D method")
    pass


d = D()
d.meth()