print("Enter your number a:")
num = input()
print("Enter your number b:")
num1 = input()
try:
    print("The sum of these number is ",
          int(num)+int(num1))
except Exception as e:
    print(e)
print("Good")