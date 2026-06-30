# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

"""
Explanation
A set can only contain hashable (immutable) elements.
A list is mutable (changeable), so it is unhashable.
Therefore, Python does not allow a list inside a set, and the set cannot even be created.
Correct Statement

No. A list cannot be contained in a set because lists are mutable (unhashable). Therefore, you cannot change the values inside a list in a set, since such a set is invalid.
"""