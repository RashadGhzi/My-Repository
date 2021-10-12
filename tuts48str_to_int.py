list1 = ["10", "20", "30"]
for item in range(len(list1)):
    list1[item] = int(list1[item])

print(list1[0]+1)
print(len(list1))

item = ["5","10","15"]
result = list(map(int,item))
print(result)
print(result[1]+result[2])