from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def display_item(self):
        pass

class liker_person(A):
    def __init__(self):
        self.height = 10
        self.breadth = 5

    def display_item(self):
        return self.height*self.breadth

like = liker_person()
print(like.display_item())