#!/usr/bin/python3

class Base():
    name = "Name : Jayson San Buenaventura"
    def base_method(self):
        print("This is a Base class!")

    def greet(self):
        print("Hello there, Im from Base class")

class Child(Base):
    team = "Team : coderz"
    def child_method(self):
        print("This is a Child class!")

    def greet(self):
        print("Hello there, Im from Child class")

class anotherChild(Child):
    members = "Members : 5"
    def another_child_method(self):
        print("This is anotherChild class!")

# Object for anotherChild class
object3 = anotherChild()
object3.base_method()
object3.child_method()
object3.another_child_method()

# Overrides Base class if the same method is existed in anotherChild class
object3.greet()  

# Inherit Base class and Child class in anotherChild class
print("\n")
print(object3.name)
print(object3.team)
print(object3.members)
