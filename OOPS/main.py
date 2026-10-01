# class Factory:

#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your project derails are Material:{self.material}, Pockets:{self.pockets}, Zips:{self.zips}")
        

# reebok = Factory("Leather",3,2)

# campus = Factory("nylon",3,3)

# reebok.show()


# class Animal:

#     def __init__(self,age): #instance attribute
#         self.age = age 

#     def show(self): #instance method
#         print(f"How are you your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("How are you brother")

#     @staticmethod
#     def static():
#         print("How are you again")

# obj = Animal(12)

# obj.hello()

### INHERITANCE

# class FactoryMumbai: # Parent Class
#     a = "I am an attribute mentioned inside a Factory Mumbai"
#     def hello(self):
#         print("Hello i am method mentioned inside Factory Mumbai")

# class FactoryPune(FactoryMumbai): # Child Class
#     pass

# obj = FactoryMumbai()
# obj2 = FactoryPune()

# print(obj2.a)


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Hello your name is {self.name}")


# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)  
#         self.age = age

#     def show(self):
#         print(f"Hello your name is {self.name}, {self.age}")


# animal1 = Animal("lion")
# person1 = Human("Nabeel", 20)

# animal1.show()



# class Animal:
#     def __init__(self, name):
#         pass

# class Human:
#     def __init__(self, name, age):
#         pass

# class Robots(Animal,Human):
#     name3 = "Charlie123"

# obj = Robots()

