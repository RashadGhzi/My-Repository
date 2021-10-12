
print("Enter your age : ")
age = int(input())
if age == 18:
    print("We will think about it.")

elif age < 18 and age > 5:
    print("You can not drive.")

elif age > 18 and age < 100:
    print("You can drive.")

else:
    print("You entered an invalid keyword.")