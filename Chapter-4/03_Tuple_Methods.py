a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element
a = (1,2,3,4,5,6,7,8,9,10,False,True,"Aakash","Rohan",345.06,5)
print(type(a))

# Counting occurrences of an element
print("Counting occurrences of an element")
no = a.count(2)
print(no)

# Finding the index of an element
print("Finding the index of an element")
index = a.index(4)
print(index)
