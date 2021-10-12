"""def func1():
    print("Hello world")

func2 = func1()
del func1
func2"""


def func(num):
    if num == 0:
        return print
    if num == 1:
        return sum

print(func(1))
print(func(0))