#import time
"""time1 = time.time()
a = 1

while a <= 1000:
    print("Harry is a good boy.")
    a += 1
time2 = time.time()
print(time2-time1)

time3 = time.time()
for a in range(1001):
    print("Rashad is a bad boy.")
time4 = time.time()
print(time4-time3)"""
import time

l = time.asctime(time.localtime(time.time()))
print(l)