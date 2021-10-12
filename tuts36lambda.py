
def lamp(a,b):
    return (a+b)
print(lamp(5,6))

# This is lambda function
lamp1 = lambda a,b:a+b
print(lamp1(5,6))

a = (lambda x: x*x*x)(2)
print(a)