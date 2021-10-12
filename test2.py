
print("Welcome to our calculator")
print('Enter the number you want to calculation of:')
num1 = float(input())
a = input()
if a == '*':
    num = float(input())
    print((num1*num))

elif a == '+':
    num = float(input())
    print((num1+num))

elif a == '-':
    num = float(input())
    print((num1-num))

elif a == '/':
    num = float(input())
    print((num1/num))

else:
    print("Error")