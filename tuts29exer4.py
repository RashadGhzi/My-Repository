from random import randint
a = 1
n = randint(0,1)
print(bool(n))
if n == 1:
    print("Enter your number for star pattern:")
    star = int(input())
    for i in range(1,(star+1)):
        print(i*("*"))
elif n == 0:
    print("Enter your number for reverse star pattern:")
    star1 = int(input())
    for i1 in range(1,(star1+1)):
        print(star1*("*"))
        star1 = star1 - a