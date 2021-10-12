def is_palindrom(n):
    str_item = str(n)
    if str_item == str_item[::-1]:
        return True
    else:
        return False

def next_palindrome(n):
    while not is_palindrom(n):
        n += 1
    return n


if __name__ == '__main__':
    print('Enter the number of text cases:')
    type_num = int(input())
    list = []
    for i in range(type_num):
        print('Enter number for check palindrom or next palindrom:')
        item_list = int(input())
        list.append(item_list)
    print(list)

    for i in range(type_num):
        print(f'Number of {list[i]} next palindrom is {next_palindrome(list[i])}')