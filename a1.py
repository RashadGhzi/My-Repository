book_list = ["Physics","Math","Python basics","Bangla","C++ language"]
i = 0
try:
    while (True):
        print(f"{i+1}.{book_list[i]}")
        i = i + 1
except IndexError:
    print("No more books in library")

book_list.remove("Math")
print(book_list)

