
print("Enter 1 for sum(+). \n2 for multiple(x). \n3 for devided(/). ")
n = int(input())
if n == 1:
    print("Enter number a ")
    a = float(input())
    print("Enter number b ")
    b = float(input())
    print("The sum is ", (a+b))

elif n == 2:
    print("Enter number a ")
    a = float(input())
    print("Enter number b ")
    b = float(input())
    print("The multiple is ", (a*b))

elif n == 3:
    print("Enter number a ")
    a = float(input())
    print("Enter number b ")
    b = float(input())
    print("The devided is ", (a/b))

else:
    print("You entered an invalid keyword")