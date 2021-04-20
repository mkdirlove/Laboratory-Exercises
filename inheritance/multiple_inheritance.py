#!/usr/bin/python3

class Base():
    name = "Name : Jayson San Buenaventura"
    def base_method(self):
        print("This is a Base class!")

    def greet(self):
        print("Hello there, Im from Base class")

class Child:
    team = "Team : coderz"
    def child_method(self):
        print("This is a Child class!")

    def greet(self):
            print("Hello there, Im from Child class")
    
class anotherChild(Child, Base): # (M R O) 
    members = "Members : 5"
    def another_child_method(self):
        print("This is anotherChild class!")

# Object for anotherChild class
object3 = anotherChild()
object3.greet()

# Check the MRO
print("\n---- Method Resolution Order(MRO) ----\n")
print(anotherChild.mro())

# Method Resolution Order (M R O)
# Is the order in which Python looks 
# for a method hierarchy of classes
