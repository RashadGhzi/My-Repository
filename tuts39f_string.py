
a = "harry"
b = 4
m = ("harry",10,20)
print("This is %s %s" %(a,b))
"""
c = ("This is {1} {0}")
d = c.format(a,b)
e = c.format(b,a)
print(d)
print(e)
"""
print(f"This is {a} {b}")
print(f"This is {m[2]} {m[0]} ")