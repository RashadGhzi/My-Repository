
import time
from functools import lru_cache

@lru_cache(maxsize=1)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("grow up")
    some_work(6)
    print("like")
    some_work(6)
    some_work(6)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")
    some_work(5)
    print("phagol")

