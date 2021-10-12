# Creating a library class
# 1.Display all books from my library class
# 2.Lend books
# 3.Add books
# 4.Return books


class book_library:

    def __init__(self,library_name):
        self.library_name = library_name
        self.book_list = ["Physics","Math","Python basics","Bangla","C++ language"]


    def display_book(self):
        print(f"All books from {self.library_name} library.")
        item = 0
        try:
            while (True):
                print(f"{item+1}.{self.book_list[item]}")
                item = item + 1
        except IndexError:
            print("No more books has left.")


    def lend_books(self):
        self.display_book()
        print(f"Which book you want to lend from {self.library_name} library.")
        self.books_name = input()

        if self.books_name in self.book_list:
            print("Here is your book.")
            print("Thank you for choosing our library.")
        else:
            self.book_list.append(self.books_name)
            print(self.book_list)
            print("Your book has been updated. Now, you can take your book.")
            print("Thank you for choosing our library.")
        self.book_list.remove(self.books_name)


    def add_books(self):
        print("Enter your book name:")
        books_name = input()
        self.book_list.append(books_name)
        print("Your book has been updated.")


    def return_books(self):
        print("If you want to return book. \nThen please enter the book name : ")
        book_name = input()
        self.book_list.append(book_name)


print("Enter your name:")
your_name = input()
print(f"Hi! {your_name}. Welcome to Rashad library.")
Rashad = book_library("Rashad")

try:
    while(True):
        print("\nSelect one of this option:")
        print("1.Display all book from library."
                  "\n2.Lend books from library"
                     "\n3.Add books in your library."
                        "\n4.Return books from library.")

        option_select = int(input())
        if option_select == 1:
            Rashad.display_book()
        elif option_select == 2:
            Rashad.lend_books()
        elif option_select == 3:
            Rashad.add_books()
        elif option_select == 4:
            Rashad.return_books()
        else:
            print("error")

        print("\nIf you want to continue then press 'c' for continue or 'q' for quite.")
        exit_function = input()
        if exit_function == 'q':
            break
        elif exit_function == 'c':
            continue
        else:
            print("You entered an invalid keyword.")
            break

except Exception:
    print("Please, enter a correct option.")

