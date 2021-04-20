#!/usr/bin/python3

class Base:
    name = "Jayson San Buenaventura"
    def base_method(self):
        print("This is a Base class!")

class Child(Base):
    team = "coderz"
    def child_method(self):
        print("This is a Child class!")

# Object for base class
object1 = Base()
object1.base_method()

# Object for child class
object2 = Child()
object2.child_method()

# Inherit Base class in Child class
print(object2.name)
print(object2.team)

