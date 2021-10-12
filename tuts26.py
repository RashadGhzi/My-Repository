f = open("file.txt")
#content = f.read()
#print(content)
#content = f.read(5)
#print(content)
#f.close()
'''for line in f:
    print(line, end="")'''
content = f.readlines()
print(content[1])