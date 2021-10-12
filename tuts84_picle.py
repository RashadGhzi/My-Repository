import pickle


# cars = ["Audi","BMW","Lambourgini","Ferrari"]
# file = open("mycars.pkl","wb")
# pickle.dump(cars,file)
# file.close



file = open("mycars.pkl","rb")
item = pickle.load(file)
print(item)
file.close()




# initializing data to be stored in db
# Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 'age' : 21, 'pay' : 40000}
# Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 'age' : 50, 'pay' : 50000}
#
# # database
# db = {}
# db['Omkar'] = Omkar
# db['Jagdish'] = Jagdish
#
# # For storing
# b = pickle.dumps(db)	 # type(b) gives <class 'bytes'>
#
# # For loading
# myEntry = pickle.loads(b)
# print(myEntry)
