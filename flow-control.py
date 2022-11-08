#In python we can say && or "and"

#lets see the table of truth for AND operator
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)

#personally, i like to think in the && operator as a simple question:
#THIS and THIS are true things?
#if even one element is false, we can't answer with a confirmation.

print(5 > 2 and 2 > 1) 
#Five is higer than 2 and 2 is higher than one? Yes.

#the only True case is when both elements are true.

#&& Table of truth:
#True and True:  True
#True and False:  False
#False and True:  False
#False and False:  False

###### OR or  "or"  :B
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)

#Or Table of Truth:
#True or True:  True
#True or False:  True
#False or True:  True
#False or False:  False

#Is this OR this true?
#if any is true, the answr is true.

#Xor or ^
print("True xor True: ", True ^ True)
print("True xor False: ", True ^ False)
print("False xor True: ", False ^ True)
print("False xor False: ", False ^ False)

#Xor Table of Truth:
#True xor True:  False
#True xor False:  True
#False xor True:  True
#False xor False:  False

#Its onlt True, when both elements are diferrent


####### IF STATEMENTS

a=5
b=6
c=7

if a < b and b > a:
    print("take care of the Indentation.")

#parentesis as on maths is good practice

if (((a > b) and (b <= c)) or (c == a)) ^ (a < b):
    print("python is math friendly <3")

somethingTrue = True
trueToo = True

if somethingTrue:
    print("if enter in first condition")
elif trueToo:
    print("no matter if our elif its true, the condition above return first")
else:
    print("defaulta case")


############# WHILE LOOPS

count = 0

while count <= 10:
    print("the count is:", count)
    count += 1                          #add one and make the new result the new value of.

while count <= 20:
    if count % 2 == 0:
        print(count, "is even number")
    count += 1  

#break cuts all the iterations
while count <= 30:
    if count == 25:
        print("breaking condition")
        break
    count += 1

#continues interrupt the current iteration and goes to the next
while count <= 35:
    if count % 2 == 0:
        count += 1
        continue
    else: print(count, "is odd number")
    count += 1


##########FOR LOOPS

list = [1,2,3,4,5,6,7,8,9,10]

#iterate over a list
for element in list:
    print("iterarion number: ", element)

#give a range of numbers
for number in range(5):
    print(number) #0,1,2,3,4

for number in range(5, 10):
    print("hey!",number) #5,6,7,8,9

#range for iterate over a list (or a tuple)

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

length = len(abc) #reserved word to get the length of the list

for el in range(5,length):
    print(abc[el]) #f g h i j

################################

strings = ("hello", "world", "python", "javascript")

for el in strings:
    print("actual word: ", el)

    if el == "world":
        print("We found World!")
        break #as we found the word, break out of the loop
    
###but, look how powerfull is IN

if "world" in strings:
    print("We found World!")

if "java" not in strings:
    print("where is java?")

###### Other cool python things:

#how to order a list?

lista = [3,7,4,8,4,7,9,10]

orderedLista = sorted(lista)

print(orderedLista) #[3, 4, 4, 7, 7, 8, 9, 10] see how we dont loose repeated numbers as in sets

#ordeder and backwards 

orderedAndBack = sorted(lista, reverse=True)

print(orderedAndBack)

abclist = ["A", "c","b","C","B","a"]

orderedABC = sorted(abclist)

print(orderedABC)#['A', 'B', 'C', 'a', 'b', 'c'], remember this works in ASCII

######MATCH its like switch, and it requires python 3.10 or newer
value=4
#match value:
#    case 1:
#        print("value is 1")
#    case 4:
#        print("value is 4!")


#### Another couriosity of for loops, The Else in for loops!

list1 = ["hello","hola","python","world"]

for el in list1:
    if el == "python":
        print("found it!")
        break
else:
    print("not found :(")


#this help to avoid things like creating variables to check the not found cases

##### PASS keyword

for el in list1:
    pass

#i.e.: like saying, hey python dont worry about this i'm gonna write it later.

if 5>4:
    pass

#is for not getting error in still not developed parts of your code