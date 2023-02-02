# variables datatypes and Types

# var = 36.9
# print(var)
# var = 345.987629
# print(var)
# print(type(var))

"""
to typecast a variable into any datatype
for eg :-
str()
int()
below is the code
"""

varq = "24"
varb = "36"

var1 = 24
var2 = 36
summ = str(var1) + str(var2)
sum = int(varq) + int(varb)
print(summ, sum)


"""
to enter the number from the user
use input()
function

the number the user will enter is in  the string form always
"""

print("Please enter the number")
inpnum = input()

print("you entered", int(inpnum) +10)

print("Please first enter the number")
n1 = input()
print("Please second enter the number")
n2 = input()
# sumInt = int(n1) + int(n2)

print("the sum of the number is",int(n1)+ int(n2))
