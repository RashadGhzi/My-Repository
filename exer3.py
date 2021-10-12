print("Guess the point. \nBy guessing correct point you can win prizes.")
print("You will get 5 chances to guess correct point.")
i = 1
while i <= 5:
    num = int(input())
    if num == 18:
        print("Great job, you done it!")
        break
    elif num <= 10 and num >= 1:
        print("No, its not. Guess more point.")
    elif num <= 17 and num >= 11:
        print("Guess little more point.")
    elif num >= 26 and num <= 36:
        print("No, its not. Guess low point.")
    elif num >= 19 and num <= 25:
        print("Guess little low point.")
    else:
        print("You are out of range.")
    i = i + 1
    if i == 5:
        print("You have one more chance to guess it.")
        continue
    if i == 6:
        print("Game over.")