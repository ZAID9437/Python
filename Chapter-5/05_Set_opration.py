s = {8, 69, 25, 30}
s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}

print(len(s))#: Returns 4, the length of the set
print(s.remove(25))#: Updates the set s and removes 8 from s.
print(s)
print(s.pop())#: Removes an arbitrary element from the set and return the element removed.
print(s.clear())#: empties the set s.


print(s1.union(s2))#: Returns a new set with all items from both sets.
print(s1.intersection(s2))#: Returns a set which contains only item in both sets {8}.