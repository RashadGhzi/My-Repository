# Iteerable - __getitem__() or __iter__()
# Iterator - __next__()
# Iteration -

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())


for i in g:
    print(i)

h = "good boy"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
