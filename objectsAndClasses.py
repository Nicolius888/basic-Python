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


    def checkPrivate(self):
        return self._myPrivateVariable



#new instance of the class or new Object
newObject = Object()

#using the methods
newObject.changeSomething() #hi


#accesing the properties
print(newObject.property0) #False
print(newObject.property1) #True


#Python doesn't have the concepts of public, private or protected.
#properties (and pretty much everything then) are overwriteable.

newObject.property0 = True
newObject.property1 = False

print(newObject.property0) #True
print(newObject.property1) #False

#There is a CONVENTION, and it is just a way of NAMING VARIABLES
#to undesrstand something as "private"
#is putting an underscore in the front of the variable name.
# like _variableName
#but remember, ITS JUST A CONVENTION.

print(newObject._myPrivateVariable) #this is private

#the idea is to not modify any variable that starts with underscore. 
#but its still techincally possible.

#The correct way of modifying the private variable is with adding a method to do the work.
newObject.modifyPrivate("car")
print(newObject._myPrivateVariable) #this car is private

#Even to accesing it the ideal is to have a method to not do it directly.
print(newObject.checkPrivate()) #this car is private


#-------------------------------------------------------------------------------------


#There is static classes too
#here all the instances chare the same memory space
#i.e. all the new instances will have the same properties.

class Static:
    num  = 0 

    def add():
        Static.num += 1 #this type of class dont use self
                        #instead, they call the name of the class to modify properties.

print(Static.num) #0
Static.add()
print(Static.num) #1

#----------------------------------------------------------------------------------
#Inheritance

class myBoolean(Object): #just pass the Father class as an argument

    def checkBoolean(self):
        pass

newBool = myBoolean()

#same methods and properties:

print(newBool.checkPrivate()) #this is private
newBool.modifyPrivate("boolean")
print(newBool.checkPrivate()) #this boolean is private

#NOTE: as a good practice, aviod multiple inheritance, it is posible, but bring problems.
#To inherit from multiple fathers, just put the antecesor,
#if a "student", needs to be a "civil person" and  "biological human" too
#supose that the inheritance wa, "biological human" --> "civil person"
#just add it at the end of the chain :
#"biological human" --> "civil person"-->"student"
#student will inherit everything from biological human and from civil person.

#class biological human()
#class civil person(biological human)
#class student(civil person)

#---------------
print(dir(newBool))#to see everithing inside the class...
#---------------

#---------------------------------------------------
#Constructor

class Car():

    brand = "none"
    color = "none"

    def __init__(self, color): #__init__ its the keyword for the constructor
        self.brand = "ford"    #works to define how the instance must be initialized
        self.color = color     #to define properties throug arguments or by default.


newCar = Car("blue")
print(newCar.brand) #ford
print(newCar.color) #blue

#see __del__ to create a destructor function in the class, at the end of
#all things related to de object pyhton will invoke it and delete the object
#the garbage collector do it anyways
#and, you can use it too as del(nameOfYourInstance)

#Calling Constructors of Fathers

class SportCar(Car):

    engine = "none"

    def __init__(self, engine, color):
        self.engine = engine
        super().__init__(color)  #keyword super to call the father and then the desired method
                                   #the constructor in this case.

newSportCar = SportCar("V8", "green")

print(newSportCar.brand) #ford
print(newSportCar.color) #green
print(newSportCar.engine) #V8





