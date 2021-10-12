class emplyee:
    """def __init__(self,aname,bname):
        self.aname = aname
        self.bname = bname"""
        #self.email = f"{self.aname}_{self.bname}@gmail.com"

    # def print_employee(self):
    #     return f"The emloyee is {self.aname}_{self.bname}"

    @property   # This is encapsulation. now, this function is a property of class
    def email(self):
        if self.aname == None or self.bname == None:
            return "Please, set your email."
        else:
            return f"{self.aname}_{self.bname}@gmail.com"

    @email.setter   # First in at @email.setter and then function email
    def email(self,string):
        print("good boy")
        name = string.split("@")[0]
        self.aname = name.split("_")[0]
        self.bname = name.split("_")[1]

    @email.deleter
    def email(self):
        self.aname = None
        self.bname = None


"""liker_boy = emplyee("bd","supporter")
print(liker_boy.print_employee())
print(liker_boy.email)"""

liker_boy = emplyee()
liker_boy.email = "us_lucky@gmail.com"
print(liker_boy.email)
print(liker_boy.aname)
print(liker_boy.bname)

del liker_boy.email
print(liker_boy.email)
