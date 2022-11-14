#make a program that prints 100 to 0 in inversed order.
#two different solutions...

#count = 100

#while count > 0:
#    print(count)
#    count -= 1

#-------------------------------
#rango_1_100 = range(1,101)       #see how we can save a range in a variable, awesome.

for i in reversed(range(1,101)):  #and how we literally say to the for loop to go backwards.
    print(f"- {i}")
