# Method Overriding

class Animal:
    def show(self):
        print("Hello, How are you")

class Human(Animal):
    def show(self):
        print("I am Fine")

obj = Human()
obj.show()