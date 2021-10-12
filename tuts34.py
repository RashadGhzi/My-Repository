"""
# 1, 1, 2, 3, 5, 8, 13 this is fibonacci series.
# This is recursive finction
# This function can call himself
def fib (n):
    if n == 1:
        return  1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else :
        return fib(n-1)+fib(n-2)
print(fib(5))
"""

# This is recursive finction
# This function can call himself
def cal(n):
    if n == 1:
        return 2
    elif n == 2:
        return 2
    elif n == 3:
        return 2
    else:
        return cal(n-1)*cal(n-2)*cal(n-3)
print(cal(5))


"""
# This is recursive finction
# This function can call himself
def factorial(n):
    if (n == 1) | (n == 0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
"""

# This is itrative function
# This function can't call himself
"""def factorial(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(1,(n+1)):
            fact = fact * i
        return fact
print(factorial(5))
"""