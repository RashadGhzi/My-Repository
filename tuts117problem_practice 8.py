
if __name__ == '__main__':
    print('Enter your number that you want multiplication table of:')
    num = int(input())

    list = []
    for i in range(1 ,(10 +1)):
        if i == 5:
            list.append(f'{num} x {i} = {(num * i ) +5}')
            continue
        list.append(f'{num} x {i} = {num *i}')
    print(list)

    rohan_list = []
    for i in range(1, (10 + 1)):
        rohan_list.append(f'{num} x {i} = {num * i}')
    print(rohan_list)

    for i in range(10):
        if list[i] != rohan_list[i]:
            print(f"{rohan_list[i]} not macthed {list[i]}. \n{list[i]} this calculation is wrong.")





    # import random
    #
    # def rohanMultiplication(number):
    #     wrong = random.randint(0, 9)
    #     table = [i * number for i in range(1, 11)]
    #     table[wrong] = table[wrong] + random.randint(0, 10)
    #     return table
    #
    #
    # def isCorrect(table, number):
    #     for i in range(1, 11):
    #         if table[i - 1] != i * number:
    #             return i - 1
    #
    #     return None
    #
    #
    # if __name__ == "__main__":
    #     # print(rohanMultiplication(7))
    #     number = int(input("Enter a number: "))
    #     myTable = rohanMultiplication(number)
    #     print(myTable)
    #     wrongIndex = isCorrect(myTable, number)
    #     print(f"The table is wrong at index {wrongIndex}")

