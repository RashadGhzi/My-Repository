
def fun1(a,b):
    print("You are in function1.")
    print("The sum is ", (a+b)/2)
fun1(5,7)
def func2(a,b):
    mul  = (a*b)
    return mul
v = func2(5,8)
print(v)
def func3(a,b):
    """ This is a function which will calculate two function
        This function is dosen't work three for function."""
print(func3.__doc__)