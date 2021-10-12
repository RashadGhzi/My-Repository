'''
f = open("file2.txt", "a")
f.write("Harry is a good boy.\n")
f.close()
'''

f = open("file2.txt", "r+")
a = f.read()
print(a)
f.write("\nThank you.")
f.close()