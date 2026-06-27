"""
Operators in Python
Following are some common operators in python:
1. Arithmetic operators: +, -, *, / etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not
"""

# 1. Arithmetic operators: +, -, *, / etc.
print("1. Arithmetic operators: +, -, *, / etc.")
a = 34
print("Value Of A Is like :- ",a)

b = 4
print("Value Of B Is like :- ",b)

c = a + b
print("Addition Of A And B Is :- ",c)

c = a - b
print("Subtraction Of A And B Is :- ",c)

c = a * b
print("Multiplication Of A And B Is :- ",c)

c = a / b
print("Division Of A And B Is :- ",c)

# 2. Assignment operators: =, +=, -= etc.
print("2. Assignment operators: =, +=, -= etc.")
a = 4 - 2 
print("Value Of A Is :- ",a)

b =  6
print("Value Of B Is :- ",b)

b += 3 #b = b + 3
print("Value Of B After Addition Is :- ",b)

b -= 3 #b = b - 3
print("Value Of B After Subtraction Is :- ",b)


# 3. Comparison operators: ==, >, >=, <, != etc.
print("3. Comparison operators: ==, >, >=, <, != etc.")
a = 5 > 4
print("5 > 4 ? True:False:- ",a)

b = 5 < 4
print("5 < 4 ? True:False:- ",b)

c = 4 == 5
print("4 == 5 ? True:False:- ",c)

d = 4 >= 5
# d = 4 <= 5
print("4 >= 5 ? True:False:- ",d)

e = 4 != 5
# e = 5 != 5
print("4 != 5 ? True:False:- ",e)

# 4. Logical operators: and, or, not
print("4. Logical operators: and, or, not")

a = True or False
print("Truth Table Of 'or' Operator")
print("True Or False Is :- ",True or False)
print("True Or True Is :-",True or True )
print("False Or True Is :-",False or True )
print("False Or True Is :-",False or False )

print("Truth Table Of 'and' Operator")
print("True and False Is :- ",True and False)
print("True and True Is :-",True and True )
print("False and True Is :-",False and True )
print("False and True Is :-",False and False )

print("Truth Table Of 'not' Operator")
print("not True Is :- ",not True)
print("not False Is :- ",not False)
print("not True and False Is :- ",not True and False)