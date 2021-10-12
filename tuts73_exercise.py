dict = {}
print("How many item you want to add in your dictionary.")
item_num = int(input())

count_for_condition = 1
while(count_for_condition <= item_num):
    print(f"Enter item {count_for_condition}:")
    item_name = input()
    dict.update({count_for_condition :item_name})
    count_for_condition = count_for_condition + 1


while(True):
    print("Chosse your option.")
    print("1.List comprehension.\n"
                "2.Dictionary comprehension.\n"
                        "3.Generator comprehension.\n"
                                "4.Set comprehension.")

    choose_option = int(input())
    if choose_option == 1:
        i = [value for key,value in dict.items()]
        print(i)
        print(type(i))
    elif choose_option == 2:
        i = dict
        print(i)
        print(type(i))
    elif choose_option == 3:
        i = (item for key,item in dict.items())
        print(i.__next__())
        print(i.__next__())
        print(i.__next__())
        print(type(i))
    elif choose_option == 4:
        i = {item for item1,item in dict.items()}
        print(i)
        print(type(i))

    print("Enter 'q' for exit the program. \nEnter 'c' for continue.")
    Select = input()
    if Select == 'q':
        break
    elif Select == 'c':
        continue
    else:
        break