import json
# JSON = Java Scripts Object Notation
# JSON is a data exchange format similar to XML

# data = '{"var1":"harry", "var2":56}'
# # data = '[10,20,30,40,50]'
# print(data)
# print(type(data))

# parsed = json.loads(data)    # It is convert a string to a json dictionary .
# # print(parsed[1])
# # print(parsed[2])+
# print(type(parsed))
# for key,value in parsed.items():
#     print(f"{key}:{value}")





# dict = {
#     "ChannelName":"CodeWithHarry",
#     "cars":["bmw","audi","lamborgini","ferrari"],
#     "item":("computer","phone","keyboard"),
#     "condition":False
# }

# output = json.dumps(dict)            # It is used to convert a dictionary to json string for java scripts.
# print(type(output))
# print(output)




dict = {
    "ChannelName":"CodeWithHarry",
    "cars":["bmw","audi","lamborgini","ferrari"],
    "item":("computer","phone","keyboard"),
    "value":[20,30,40,50,60],
    "condition":False
}

result = json.dumps(dict,indent=5)
print(result)
print(type(result))