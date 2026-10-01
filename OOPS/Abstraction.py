from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(abstract):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        print("I have created perimeter")
        
    def area(self):
        print("I have created area")
        


class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("I have created perimeter")

    def area(self):
        print("I have created area")

obj = Circle(7)
obj2 = Square(12)