
a = input("What is your name: ")
b = input("How much do you earn: ")
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello {a}")


# 1000 lines taking 1 hour
# Task - Write about 2 built in exception

# c = input("Enter your name: ")
# try:
#     print(c)

# except Exception as e:
#     if c == "harry":
#         raise ValueError("Harry is blocked he is not allowed")

#     print("Exception handled")


# x = 5
# if x < 10:
#    raise ValueError('x should not be less than 10!')
