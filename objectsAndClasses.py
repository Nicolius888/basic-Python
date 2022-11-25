#Class declaration structure
#keyword + name + :
class Object:
    #The properties of the future objects are just variables
    property0 = False
    property1 = True

    _myPrivateVariable = "this is private"

    #And methods are just functions inside the class
    def changeSomething(self):   
        print("hi")
        pass
    #note: we are still not using the "self", but,
    # without the self we get a "TypeError: changeSomething() takes 0 positional arguments but 1 was given"
    #from bobbyhadz.com
    #Python automatically passes self to the class method when it is called, 
    #so a method that takes no arguments gets passed one which causes the error.

    def modifyPrivate(self, thing):
        self._myPrivateVariable = f"this {thing} is private"
        #self is needed to use the variable of the class;
        #without it we are declaring a new variable with the same name
        #but just existent inside the scope of this function.

#new instance of the class or new Object
newObject = Object()

#using the methods
newObject.changeSomething()


#accesing the properties
print(newObject.property0)
print(newObject.property1)


#Python doesn't have the concepts of public, private or protected.
#properties (and pretty much everything then) are overwriteable.

newObject.property0 = True
newObject.property1 = False

print(newObject.property0)
print(newObject.property1)

#There is a CONVENTION, and it is just a way of NAMING VARIABLES
#to undesrstand something as "private"
#is putting an underscore in the front of the variable name.
# like _variableName
#but remember, ITS JUST A CONVENTION.

print(newObject._myPrivateVariable)

#the idea is to not modify any variable that starts with underscore. 
#but its still techincally possible.

#The correct way of modifying the private variable is with adding a method to do the work.
newObject.modifyPrivate("car")
print(newObject._myPrivateVariable)
