import datetime
def gettime():
    return datetime.datetime.now()
damn = 1
time = ["morning", "night"]
time1 = ["morning", "noon", "night"]

print("Welcome to our health management system.")
print("1.Harry. \n2.Rohan. \n3.Hammad.")
name = int(input("Please, select your name.\n"))
if name == 1:
    print("Hi! Harry. \nSelect one of these.")
    print("1.Exercise. \n2.Food.")
    health = int(input())
    if health == 1:
        with open("harry1.txt", "a") as w:
            print("Harry, please tell us what type of exercise you are doing in two times. If no than write no.")
            while damn <= 2:
                print("Exercise in " +time[(damn-1)])
                exer = input()
                w.write(str([str(gettime())])+ " : " +exer+ "\n")
                damn = damn + 1
            print("Thank you for your daily exercise details.")
    elif health == 2:
        with open("harry2.txt", "a") as w:
            print("Harry, please tell us what type of food you eat in 3 times.")
            while damn <= 3:
                print("Food eat at " +time1[(damn-1)])
                food = input()
                w.write(str([str(gettime())])+ " : " +food+ "\n")
                damn = damn + 1
            print("Thank you for your daily food details.")
    else:
        print("You entered an invalid keyword.")


elif name == 2:
    print("Hi! Rohan. \nSelect one of these.")
    print("1.Exercise. \n2.Food.")
    health = int(input())
    if health == 1:
        with open("rohan1.txt", "a") as w:
            print("Rohan, please tell us what type of exercise you are doing in two times. If no than write no.")
            while damn <= 2:
                print("Exercise in " +time[(damn-1)])
                exer = input()
                w.write(str([str(gettime())])+ " : " +exer+ "\n")
                damn = damn + 1
            print("Thank you for your daily exercise details.")
    elif health == 2:
        with open("rohan2.txt", "a") as w:
            print("Rohan, please tell us what type of food you eat in 3 times.")
            while damn <= 3:
                print("Food eat at " +time1[(damn-1)])
                food = input()
                w.write(str([str(gettime())])+ " : " +food+ "\n")
                damn = damn + 1
            print("Thank you for your daily food details.")
    else:
        print("You entered an invalid keyword.")


elif name == 3:
    print("Hi! Hammad. \nSelect one of these.")
    print("1.Exercise. \n2.Food.")
    health = int(input())
    if health == 1:
        with open("hammad1.txt", "a") as w:
            print("Hammad, please tell us what type of exercise you are doing in two times. If no than write no.")
            while damn <= 2:
                print("Exercise in " +time[(damn-1)])
                exer = input()
                w.write(str([str(gettime())])+ " : " +exer+ "\n")
                damn = damn + 1
            print("Thank you for your daily exercise details.")
    elif health == 2:
        with open("hammd2.txt", "a") as w:
            print("Hammad, please tell us what type of food you eat in 3 times.")
            while damn <= 3:
                print("Food eat at " +time1[(damn-1)])
                food = input()
                w.write(str([str(gettime())])+ " : " +food+ "\n")
                damn = damn + 1
            print("Thank you for your daily food details.")
    else:
        print("You entered an invalid keyword.")

