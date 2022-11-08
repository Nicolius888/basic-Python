#Python session using types, and running Python 3.9, October 24, 2022.

a = 5

print(type(a))
print(id(a))
print(a)

a = 10  

print(type(a))
print(id(a))#id is to see the number of the memory location

print(a)

#Important, this basic types are INMUTABLE, 
#you can't modify, yes overwrite
#string = "hello"
# string[0] = "j" - this is modifying, not overwriting, python throws error in this cases.


#as we see, we get different id's, i.e. different memory locations.


#####################tuples and lists:

tuple = (3,3,3)
list = [9,9,9] 

print(tuple, list)

print(type(tuple),type(list))

#just remember, the big difference with this two is that tuples are INMUTABLE and lists are MUTABLE, 
#imagine that they are the same but Tuples behave like constants and lists behave like variables.
#p.s.: anyways you can override everithing...


####################let's see methods:

list.append("hello")
list.append("world")
list.append("hello")

print(list)

#list.remove("world")
#list.append("Nico")
#print(list)

list.remove("hello")  #remove method delete the element you want, but append always go to the end.
                      #if theres two equals it deletes the first
print(list)     
list.append("nico")
print(list)           #this gives us [9, 9, 9, 'world', 'nico']

list.remove(list[2])  #the index works too!.
print(list)

print(list.append(tuple)) #appends but prints None
print(list)               # but you get the idea, we can append e.g. tuples to lists, or lists to lists. 
                          #(not lists to tuples, not tuples to tuples, .APPEND() IS A LISTS METHOD)

############dictionary:

myDictionary = {
    "key": "value",
    "key2": 34,
    "anotherKey": "blabla"
}

print(type(myDictionary))
print(myDictionary["anotherKey"]) 

#NO:
#print(myDictionary.key)
#print(myDictionary[0]) 

words = myDictionary["key"]    #first, we declare words as my key
myDictionary["key"] = "value2" #then, we change the key

print(words)                   #but now, word is a pointer or his own memory location?

                               #it prints "value", not "value2"
                               #so is his own memory location
#we can even check the memory id                              
print(id(words))                  #139675395546672
print(id(myDictionary["key"]))    #139675392937840                           

#So we can conclude that, asigning a key from a dictionary to a variable, 
#even if it looks like its just a reference
#in the moment it is asigned, python creates a copy.

#####deleting keys
#there's two ways

newDict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6
}

#we have pop, it delets and then retrns it
print(newDict.pop("3"))#3
print(newDict)#{'1': 1, '2': 2, '4': 4, '5': 5, '6': 6}

#as it returns it, we can asign the returned value to a new variable
oldValue = newDict.pop("4")
print(oldValue, newDict)# 4 {'1': 1, '2': 2, '5': 5, '6': 6}

#we also can give it a second method as default return value, in a case when the key is not founded in our list.
print(newDict.pop("9", "not found"))#not found


#####del keyword:
#it is the same but it doesnt return the element

# deletedEl = del newDict["2"] , this gives error
del newDict["1"]
print(newDict)#{'2': 2, '5': 5, '6': 6}




#####we have SETS too, (conjuntos en español, lo aclaro especialmente porque es el unico que usa un termino bien distinto)

conjunct = {1,2,3,1,2,3,4}

#it is the same as lists BUT, it doesnt allow repeated elements.
#see

print(conjunct) #{1, 2, 3, 4}

#it has Matemathics operations =)

even = {0,2,4,6,8}
oneToFive = {1,2,3,9,4,5}
oneToHello = {1,2,3,"hello",4,5}
oneToHelloWorld = {1,2,3,"hello",4,5,6, "world"}
weirdCase = {1,2,3,"c",4,5,"a",9}

#UNION

union = even | oneToFive
union2 = even | oneToHello
union3 = even | oneToHelloWorld
union4 = even | weirdCase

print(union)  # {0, 1, 2, 3, 4, 5, 6, 8, 9}, i.e. it deletes the repeated ones.and even respect the order of the numbers, see the 9.
print(union2) # it orders the numbers and leaves the string for the end.
print(union3) #{0, 1, 2, 3, 4, 5, 6, 8, 'hello', 'world'}
print(union4) # {0, 1, 2, 3, 4, 'c', 6, 5, 8, 9, 'a'} here python says "Too Much bro", without the nine the behavior is the same as above, but as we see
              # with more mixed types is more complex, its a weird behavior, better to study how sets works in the immediate future. 

#INTERSECTION

inter = even & oneToFive
print(inter) # {2,4}, i.e. it saves just the repeated elements.

#DIFFERENCE
 #it saves the elements that are not repeated in the first set

diff = even - oneToFive
print(diff)  #{0,8,6}
#weird case, this ones keep unordered.

secondDiff = oneToFive - even
print(secondDiff) #{1, 3, 5, 9}


#SIMMETRIC DIFFERENCE
#unique values in the first and in the second set

simmetric = even ^ oneToFive
print(simmetric)  # {0, 1, 3, 5, 6, 8, 9} , if you see, this are the results of the last two operation, combined.
                  # 0,6,8 are the unique values in the first set and 1,3,5,9, are the unique values in the second set
                  # 2 and 4 exist in both sets, so python keeps them outside in this case.

################################################################
#TYPES RESUME

number = 5
string = "hello world"
boolean = True
float = 5.4
list = [1,2,3,4,5]
tuples = (1,2,3,4,5)
dictionaries = {"a":1,"b":2,"c":3,"d":4}
set = {1,2,3,1,2,3} #{1,2,3}

################################################################
#some typical methods

myText = "hello Beautiful, beautiful wOrld"

print(myText.capitalize()) #Hello beautiful, beautiful world

print(myText.title()) #Hello Beautiful, Beautiful World 

print(myText.upper()) #HELLO BEAUTIFUL, BEAUTIFUL WORLD

print(myText.lower()) #hello beautiful, beautiful world

print(myText.replace("e", "i")) #hillo Biautiful, biautiful wOrld

print(myText.find("wOrld")) #27

print(myText.find("world")) # -1 (don't exist)

#we can make a list from a string
print(myText.split()) #['hello', 'Beautiful,', 'beautiful', 'wOrld']

#but supouse we dont want the commas (look "Beautiful,")

# we can split from the commas
print(myText.split(',')) # ['hello Beautiful', ' beautiful wOrld']

#but this its not so elegant

#lets try combined methods
print(myText.replace(",", "").lower().split()) #['hello', 'beautiful', 'beautiful', 'world'], now this is elegant

myList = ["hola", "mundo", "!"]

print(" ".join(myList)) #i.e. Join by this character - #hola mundo !

print("".join(myList)) #holamundo!

print("-".join(myList)) #hola-mundo-!

print("-\_ 0_o _/-".join(myList)) #hola-\_ 0_o _/-mundo-\_ 0_o _/-!

#make a help(str) in the terminal an you can see all the string methods
#the same runs for every type.

#crazy feature:

num = "44" #string with numbers

print(num.isnumeric()) #True
print(num.isdecimal()) #True
print(num.isdigit()) #True
#python knows there are a number in the string.


#...
print(myText.lower().islower()) #True
print(myText.isupper()) #False
print(myText.istitle()) #False


######################
######OPERATORS#######
######################

X = 300
Y = 500

print(
   X+Y,#800
   X-Y,#-200
   X*Y,#150000
   Y/X, #1.6666666666666667 division operator
   Y//X,#1 floored division operator
   X%Y, #300
   X-200, #100
#  myText - "d" #unsupported operand type for -: 'str' and 'str'
)


#some examples of this bad boys

a = 2
b = 2
print(a/b) #1.0
print(a//b) #1

print(a/3)#0.6666666666666666
print(a//3)#0

#so we conclude that they make bassically the same operation BUT // aplies a floor to the result.

#from brainly.in
#'/' is used for the normal division of two numbers.

#'//' is used to obtain the smallest integer nearest to the quotient obtained by dividing two numbers.

#remember the difference between .floor() and .ceil() in javascript
#you guess it, this works as floor.

#Power operator 

print(a**b) # 2^2 = 4
print(a**2) # 2^2 = 4
print(a**3) # 2^3 = 8
print(a**-1) # 0.5
print(a**-2) # 0.25

#####ASIGNATION
#this works for every math op.
#operation plus asignation/overwrite:
a += b
a -= b
a *= b
a /= b
a %= b
a **= b  
a //= b

###comparation
#this are classics
# ==, !=, >, <=, >=

#indentity
# is, is not

#membership
# in, not in

##others assignations to see next
# &=
# |=
# ^=
# <<=
# >>=


#bit: &, |, ^, ~, <<, >>.
#not confuse with the set operators, these work different here.

#to exercise make an import math
#and search what that library can do.
#help(math) or google the docs

import math
myInt = 2.66666
print(math.ceil(myInt))#3
print(math.pi)#3.141592653589793