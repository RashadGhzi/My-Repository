
#___________________________List comprehension_____________________________#

# list = []
# for item in range(20):
#     if item%3 == 0:
#         list.append(item)
# print(list)

# print([item for item in range(20) if item%3 == 0])



#______________________________Dictionary comprehension_________________________#

# print({item for item in range(20) if item%2 == 0})

# dict = {}
# for item in range(20):
#     if item%2 == 0:
#         dict.update({item :f"Like {item}"})

# print(dict)
# print({value:key for key,value in dict.items()})




#_____________________________List comprehension_________________________________#

# print([item for item in ["item1", "item2", "item3",
#                             "item1", "item3", "item4"]])



#_____________________________Set comprehension_________________________________#

# print({item for item in ["item1", "item2", "item3",
#                             "item1", "item3", "item4"]})



#____________________________Parenthesis(generator) comprehension_________________________________#

even = (item for item in range(20) if item%2 == 0)
print(type(even))
print(even)
print(even.__next__())
print(even.__next__())
for item in even:
    print(item)
    
