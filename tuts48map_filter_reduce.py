#_________________MAP FUNCTION___________________#
# def square(x):
#     return x*x
# def cube(x):
#     return x*x*x
# func = [square,cube]

# for item in range(5):
#     num = list(map(lambda x:x(item),func))
#     print(num)

# num = 5
# print(list(map(lambda x:x(num),func)))


#_________________FILTER FUNCTION___________________#
# item = [1,2,3,4,5,6,7,8,9]
# def numbers(num):
#     return num>4

# print(list(map(numbers,item)))
# print(list(filter(numbers,item)))  # In filter function false will be remove automatically


#_________________REDUCE FUNCTION___________________#
from functools import reduce
num_list = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y, num_list)          # By reduce function we can summation number.
print(sum)