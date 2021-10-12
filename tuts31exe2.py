# This program is for daily note. You can note here your daily exercise and food information.
#  In option 1 you can write here your daily exercise and food information.
#  In option 2 you can see your daily exercise and food information.
import datetime
def gettime():
    return datetime.datetime.now()
try:
    print("Welcome to our health management system.")
    print("Choose your option.")
    print("1.Log. \n2.Retrieve.")
    option = int(input())

    if option == 1:
        def harry1():
            damn = 0
            time = ["morning", "evening"]
            with open("harry1.txt", "a") as exer:
                print("What type of exercise you are doing in a day. If no then write no.")
                while damn < 2:
                    print("Type of exercise in " +time[damn])
                    item = input()
                    exer.write(str([str(gettime())]) + " : " + item + "\n")
                    damn = damn + 1
                    exer.close()
                print("Thank you, for your information.")

        def harry2():
            damn = 0
            time2 = ["morning", "noon", "night"]
            with open("harry2.txt", "a") as exer:
                print("What type of food you eat in a day.")
                while damn < 3:
                    print("Type of food at " +time2[damn])
                    item = input()
                    exer.write(str([str(gettime())]) + " : " + item + "\n")
                    damn = damn + 1
                    exer.close()
                print("Thank you, for your information.")

        def rohan1():
            damn = 0
            time = ["morning", "evening"]
            with open("rohan1.txt", "a") as exer:
                print("What type of exercise you are doing in a day. If no then write no.")
                while damn < 2:
                    print("Type of exercise in " +time[damn])
                    item = input()
                    exer.write(str([str(gettime())]) + " : " + item + "\n")
                    damn = damn + 1
                    exer.close()
                print("Thank you, for your information.")

        def rohan2():
            damn = 0
            time2 = ["morning", "noon", "night"]
            with open("rohan2.txt", "a") as exer:
                print("What type of food you eat in a day.")
                while damn < 3:
                    print("Type of food at " +time2[damn])
                    item = input()
                    exer.write(str([str(gettime())]) + " : " + item + "\n")
                    damn = damn + 1
                    exer.close()
                print("Thank you, for your information.")

        def hammad1():
            damn = 0
            time = ["morning", "evening"]
            with open("hammad1.txt", "a") as exer:
                print("What type of exercise you are doing in a day. If no then write no.")
                while damn < 2:
                    print("Type of exercise in " +time[damn])
                    item = input()
                    exer.write(str([str(gettime())]) + " : " + item + "\n")
                    damn = damn + 1
                    exer.close()
                print("Thank you, for your information.")

        def hammad2():
            damn = 0
            time2 = ["morning", "noon", "night"]
            with open("hammad2.txt", "a") as exer:
                print("What type of food you eat in a day.")
                while damn < 3:
                    print("Type of food at " +time2[damn])
                    item = input()
                    exer.write(str([str(gettime())]) + " : " + item + "\n")
                    damn = damn + 1
                    exer.close()
                print("Thank you, for your information.")

    elif option == 2:
        def harry1():
            print("Here is your daily exercise information.")
            with open("harry1.txt") as exer:
                print(exer.read())
            exer.close()
            print("Thank you, for visiting our site.")

        def harry2():
            print("Here is your daily food information.")
            with open("harry2.txt") as exer:
                print(exer.read())
            exer.close()
            print("Thank you, for visiting our site.")

        def rohan1():
            print("Here is your daily exercise information.")
            with open("rohan1.txt") as exer:
                print(exer.read())
            exer.close()
            print("Thank you, for visiting our site.")

        def rohan2():
            print("Here is your daily food information.")
            with open("rohan2.txt") as exer:
                print(exer.read())
            exer.close()
            print("Thank you, for visiting our site.")

        def hammad1():
            print("Here is your daily exercise information.")
            with open("hammad1.txt") as exer:
                print(exer.read())
            exer.close()
            print("Thank you, for visiting our site.")

        def hammad2():
            print("Here is your daily food information.")
            with open("hammad2.txt") as exer:
                print(exer.read())
            exer.close()
            print("Thank you, for visiting our site.")

    else:
        print("You entered an ivalid keyword.")

    if (option == 1) | (option == 2):
        print("Select your name.")
        print("1.Harry. \n2.Rohan. \n3.Hammad")
        name = int(input())

        if name == 1:
            print("Hi! Harry. Select one these.")
            print("1.Exercise. \n2.Food.")
            item = int(input())
            if item == 1:
                harry1()
            elif item == 2:
                harry2()
            else:
                print("You entered an invalid keyword.")

        elif name == 2:
            print("Hi! Rohan. Select one these.")
            print("1.Exercise. \n2.Food.")
            item = int(input())
            if item == 1:
                rohan1()
            elif item == 2:
                rohan2()
            else:
                print("You entered an invalid keyword.")

        elif name == 3:
            print("Hi! Hammad. Select one these.")
            print("1.Exercise. \n2.Food.")
            item = int(input())
            if item == 1:
                hammad1()
            elif item == 2:
                hammad2()
            else:
                print("You entered an invalid keyword.")

        else:
            print("You entered an invalid keyword.")

except Exception as error:
    print(error, "\nPlease enter a valid keyword.")