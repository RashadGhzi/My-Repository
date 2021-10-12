from random import randint

def name_change(nameList):

    first_name = []
    last_name = []

    for i in nameList:
        first_name.append(i.strip().split(" ")[0])

    for i in nameList:
        last_name.append(i.strip().split(" ")[1])

    num = 0
    item = []
    while num < len(first_name):
        rand = randint(0,len(first_name)-1)
        print(f'{first_name[num]} {last_name[rand]}')
        num += 1
        item.append(rand)


if __name__ == '__main__':
    print('How many of your friends name you want select for fun game? \nSelect your number:')
    name = int(input())
    print('Enter your friends name:')

    nameList = []
    for i in range(name):
        friendName = input(f'Friend No.{i+1} : ')
        nameList.append(friendName)

    # nameList = ['Rohit shetty','Rohan das','Sharukh Khan','Varun dawan']
    name_change(nameList)
