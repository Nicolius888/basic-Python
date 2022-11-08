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


####IF STATEMENTS

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


##while

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