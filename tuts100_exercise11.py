import re

str = '''Email: northamerica@tata.com
email = rashadarsh78@gmail.com
priya@yahoo.com
email = meeting @2pm
Website: www.northamerica.tata.com
shubhamg199630@gmail.com
harrygoodboy@gamil.com
Directions: View map fass
indian no. +91 5588-940010
harry bhai lekin
indian no. ++91 5588-000000'''

item = re.compile(r'\S+@\S+')
item_1 = item.findall(str)
print(item_1)

i = 1
for email in item_1:
    with open('harry_larry.txt', 'a') as file:
        file.write(f'Email_{i}:{email}\n\n')
    i += 1