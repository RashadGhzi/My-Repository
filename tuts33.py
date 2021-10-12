"""
gl = 50
def harry (a):
    #gl = 20    #local
    global gl   # This will take global
    gl = gl + 10
    print(a,"This is function.")
    print(gl)
harry("We are in function")
"""

l = 100
def harry1():
    l = 120
    def harry2():
        global l
        l = 30
        print(l)
    harry2()
    print(l)

harry1()
print(l)
