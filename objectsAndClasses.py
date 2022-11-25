#Class declaration structure
#keyword + name + :
class Object:
    #The properties of the future objects are just variables
    property0 = False
    property1 = True

    #And methods are just functions inside the class
    def changeSomething(self):   
        print("hi")
        pass
    #note: we are still not using the "self", but,
    # without the self we get a "TypeError: changeSomething() takes 0 positional arguments but 1 was given"
    #from bobbyhadz.com
    #Python automatically passes self to the class method when it is called, 
    #so a method that takes no arguments gets passed one which causes the error.

#new instance of the class or new Object
newObject = Object()

#using the methods
newObject.changeSomething()

#accesing the properties
print(newObject.property0)
print(newObject.property1)





