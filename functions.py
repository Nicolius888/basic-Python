#functions are the best way to reutilize code.
#they must be like modules, i.e.: just one action by function.

#the structure is very minimalist
# def initializer + name  + parameters():
#   +body

#myFunc("World") here, before defining the function is not suported
#the interpreter goes from up to down strictly.

def myFunc(name):
    print(f"Hello {name}!")

myFunc("World")

#if the argument does not receive parameters, we get an error, and the execution stops.
#myFunc();

def maths(a, b):
    
    def add(a, b):
        print(a + b)

    def rest(a, b):
        print(a - b)
    add(a, b)
    rest(a, b)

#is valid to declare functions inside fuctions,
#remember to invoke and pass the parameters...

maths(5, 5)
#10
#0

#----------------------------------------

#declared inside functions variables belong to that scope only.

def myFunc2(name):
    temp = 22
    print(f"hello {name}, today's temperature is {temp}` celcius degrees.")

myFunc2("nico")
#   print(temp) # we get a temp is not defined

#but the "contrary motion" is valid
#using a outside already declared function inside of a function

temperature = 20

def myFunct3(name):
    temp = temperature
    print(f"hello {name}, today's temperature is {temp} celcius degrees.")

myFunct3("nico")


#-------------------------------
#in the case of repeated name between global scope and local scope,
#inside functions:  LOCAL SCOPE WINS.

number = 5

def printer():
    number = 2
    print(number)

printer() #2 goes to his own scope
print(number) #5 goes to local scope

#this is called "Variable Shadowing", is used commonly to temporally overwrite values.

#the variation of this case is using the Global reserved word:

def printerG():
    global number    #we say, use the global for "number"
    number = 55      #and here, we modify the GLOBAL variable
    print(number)

printerG()    #55 modified here
print(number) #55 new value here



#----------------------------------------------------------------------------------------

#default parameter for an argument

def sayHello(name="World"):
    print(f"Hello {name}!")

sayHello()       #Hello World!
sayHello("Paco") #Hello Paco!

#The only rule here is :
#The optional default parameters must to be all or the declared lasts.<--------

#def add2(a, b=2, c):  #<-------INVALID
def add2 (a, b, c=2): # <-------VALID
    print(a + b + c)

def add3 (a=2, b=2, c=2): # <-------VALID
        print(a + b + c)

add2(2,2,3) #7 - call overwriting c
add2(2,2)   #6 - call without parameter for c
add3()      #6 - can call without passing parameters
add3(7,8,9) #24 - call overwriting the 3 arguments
add3(3)     #7 - the value its always for the firsts arguments
            #e.g.in the add3 example, if we just pass 1 parameter 
            #it always is asigned to a,
            #we never can pass a number just for b or c
            # just a, or a & b, etc.

#BUT there is something else
#we can name the arguments when invoking

add3(a=2,c=2,b=2) #6 - and even in any order
add3(a=2,c=2)     #6 - or in any order, and even just with some of the parameters
add3(c=2)         #6


#--------------------------------------------------------------------------------------

#Variable *arguments

#instead of having lots of arguments...
#e.g.
# def add4(a,b,c,d,e,f,h,g,...)

def add4(*args):
    adding = 0
    for arg in args:
        adding += arg
    print(adding)

add4(2,3,4,5,6,7,8,9) #44

#if we print the *args, it is a tuple, so its just an inalterable list
def add4(*args):
    print(args)

add4(2,3,4,5,6,7,8,9) #(2, 3, 4, 5, 6, 7, 8, 9)

#btw the word args is just a convention, as the letter i in a for loop for example.

#----------------------------
#VARIATION: **kwargs

#its kind of the same, but when printed we see it is a dictionary, instead of a tuple

def add5(**kwargs):
    print(kwargs)

add5(myKey = "myValue", otherKey = "other value", aString = "yep, a string.")

#------iterating

def add6(**kwargs):
    for key, value in kwargs.items():  # <-------this deserves his own research xD,
        print(f"{key} = {value}")      # its just a dictionary method, but very interesting...

add6(myKey = "myValue", otherKey = "other value", aString = "yep, a string.")

#------

def kw(**kwargs):
    if kwargs["myCar"] == "cool car":
        print("you have a " + kwargs["myCar"])

kw(myCar = "cool car")
#kw()
#kw(myCar = "ugly car")
#but modifying this or not decalring it at all, will lead to an error
#we can do the "name of the element IN dictionary" verification

def carVibeCheck(**kwargs):
    if "myCar" in kwargs and kwargs["myCar"] == "cool car":
        print("yeah, cool car")

carVibeCheck(myCar = "cool car") #yeah, cool car
carVibeCheck(myCar = "ugly car") #prints nothing
carVibeCheck(superCar = "coolest car") #nothing too

#inverse mode of same verification, just to have in mind other reserver word

def carVibeCheck(**kwargs):
    if "myCar" not in kwargs:
        return
    
    if kwargs["myCar"] == "cool car":
        print("you have a " + kwargs["myCar"])

carVibeCheck(myCar = "cool car") #you have a cool car

#-----------------------------------------------------------------------------------

#return notes

#when working, of course, we use return , not print
#we do this to see some result

def ret(a, b):
    return a + b

result = ret(2, 5)

print(result)

#---------
def ret(a, b):
    return a + b, a - b, a * b, a ** b, a // b

results = ret(2,5)

print(results)  #(7, -3, 10, 32, 0) - we get a tuple!
                #so ...
print(results[0])#7 - we have access to each result
print(results[3])#32 - tuple behavior: see not modify.
#print(results[0] = 12) #python: " you wish."

#some python-assignation-magic over here:
add, rest, multi, power, div = ret(3, 3)

print(add)  #6
print(rest) #0
print(multi)#9
print(power)#27
print(div)  #1


#but have in mind that this last method, requires to create assignations for all the results
#if not we have an "too many results to unpack" error

#so we have to save everithing in a tuple
#or create so many variables as results we have in return

#----------------------------
#ternary in kwargs assignment

def suma(**kwargs):
    initial = kwargs["initial"] if "initial" in kwargs else 0

                                       #some of this assignments can fail if the element
                                       #doesn't exists in our invocation, but we have the ternary tool

    final = kwargs["final"] 
    
#this means: asign kwargs[final] only if it exists in the kwargs dictionary
#if not (else) assign a value of 0.

    result = 0

    for i in range(initial, final):  #remember: i works like an index(0,1,2,3...)
        result += i                  #to avoid zero we will put final + 1

    return result

print(suma(initial = 0,final = 5))#10
print(suma(final = 5))            #10 - if we dont declare the initial number for the range,
                                  #by default it goes to zero.

#--------------------------------------------------------------
#LAMBDA FUNCTIONS 
#or anonymus functions
#they are like arrow functions if you familiarized with JS

anon = lambda: print("hello lambda")
anon()

upperL = lambda name="world": name.upper()
print(upperL("nico")) #NICO
print(upperL())       #WORLD

#structure:
#var name + lambda keyword + arg, arg, arg: function body

addL = lambda a, b: a + b   #they don't need return!
print(addL(2,2))#4

#generally, we use lambda for super simple functions.

add2L = lambda a, b: (a + b, a-b)

varA, varB = add2L(2,2)
print(varA, varB) #4 0






