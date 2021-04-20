#!/usr/bin/python3

class myClass1:
    def feature1(self):                       
        print("Hello from feature1.")

    def feature2(self):
        print("Hello from feature2.")

class myClass2:
    def feature3(self):
        print("Hello from feature3.")

    def feature4(self):
        print("Hello from feature4.")

class myClass3(myClass1, myClass2):
    def feature1(self):
        print("Hello from feature1 in myClass3.")

    def feature2(self):
        print("Hello from feature2 in myClass3.")
            
myClass3_obj = myClass3()

# METHOD OVERRIDE
# THIS WILL TAKE THE METHOD FROM THE ORIGIN CLASS WHICH IS myClass3
# AND IGNORE THE SAME METHODS IN OTHER CLASSES BECAUSE OF (MRO).
# feature1 and feature2 FROM myClass1 IS IGNORED.

myClass3_obj.feature1()
myClass3_obj.feature2()

myClass3_obj.feature3()
myClass3_obj.feature4()
