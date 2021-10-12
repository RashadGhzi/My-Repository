import pickle
import requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
item = requests.get(url).text
item_list = item.split("\n")
# print(item_list)
item_in_list = [item.split(',') for item in item_list if len(item)!=0]
print(item_in_list)

# file = open('text.pkl','ab')
# pickle.dump(item_in_list,file)

file_read = open('text.pkl','rb')
item_load = pickle.load(file_read)

print(item_load)