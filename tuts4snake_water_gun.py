from random import randint
print("Welcome to our snake, water and gun game")
name = input("Enter your name:\n")
print("Hi! " +name+ ".")

i = 1
a = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
cpoint  = 0
ppoint = 0

try:
    while i <= 3:
        print("Now, Your turn:")
        print("1.Snake. \n2.Water. \n3.Gun.")

        pnum = int(input())
        if pnum == min(0,pnum):
            print("Please, Enter the correct number.")
            continue
        item = ["snake","water","gun"]
        player = item[pnum-1]
        print(name+" choosed " +player)

        cnum = randint(0,2)
        computer = str(item[cnum])
        print("Computer choosed " +computer)
        if (player == computer):
            print("It's a draw.")
            cpoint += 1
            ppoint += 1
        elif (computer == "snake") & (player == "water"):
            print(f"Computer won the {a[i-1]} round.")
            cpoint += 1
        elif (computer == "water") & (player == "gun"):
            print(f"Computer won the {a[i-1]} round.")
            cpoint += 1
        elif (computer == "gun") & (player == "snake"):
            print(f"Computer won the {a[i-1]} round.")
            cpoint += 1
        else:
            print(f"{name} won the {a[i-1]} round.")
            ppoint += 1

        print("Computer point is: ",cpoint)
        print(name+" point is ", ppoint)

        if i == 2:
            print("You have one more chance.")
        print("\n")
        i = i + 1

    if (cpoint == ppoint):
        print("Oooh shit!!. This game is draw.")

    elif (cpoint > ppoint):
        print("Computer won the game. \nBetter luck next time.")

    else:
        print(f"Congratulation! {name} won the game. \nWinner Winner! Chicken Dinner.")

except Exception:
    print("Please enter a vhalid keyword.")
