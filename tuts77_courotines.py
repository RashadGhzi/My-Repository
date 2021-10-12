from time import sleep
def searcher():
    print('Searching.....')
    books = 'sharukh khan, salman khan, King-Amir khan, sarfaraz khan'
    sleep(10)

    while (True):
        text = (yield )
        if text in books:
            print('Your text is in book.')
        else:
            print('Your text is not in book.')

search = searcher()
print("search started")

next(search)
print("Next method run")
search.send("shahrukh khan")

print("Next method run")
search.send("salman khan")

print("Next method run")
search.send("sarfaraz khan")

print("Next method run")
search.send("minaz khan")
