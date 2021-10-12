with open("aaa.txt", "a") as file:
    print("Input your string. \nIf you want to stop write stop.")
    while True:
        name = str(input())
        file.write(name+"\n")
        if name == "stop":
            break
    file.close()