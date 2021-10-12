import json

dict = {5:'good', 2:'like', 1:'better', 4:'nice', 3:'excellent', (6,7,8):'mervelous', 10:float('nan')}

result = json.dumps(dict,skipkeys=True,allow_nan=True,separators=(". ", " = "),indent=5)
print(result)
print(type(result))


dict2 = {5:'good', 2:'like', 1:'better', 4:'nice', 3:'excellent'}
item = json.dumps(dict2,sort_keys=True)
print(item)
print(type(item))


# ----------------------------> Details is in python project json geeksforgeeks <-----------------------------#