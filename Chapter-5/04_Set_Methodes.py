s = {1, 5, 32, 5, 5, 1, 32,"Zaid Mansuri"} # no repetition allowed
print(s)

s.add(566)
print(s,type(s))




"""
Properties Of Sets
Sets are unordered => Elementʼs order doesnʼt matter
Sets are unindexed => Cannot access elements by index
There is no way to change items in sets.
Sets cannot contain duplicate values.
"""

"""
| Method                   | Description                                          | Example                     |
| ------------------------ | ---------------------------------------------------- | --------------------------- |
| `add()`                  | Adds a single element                                | `s.add(10)`                 |
| `update()`               | Adds multiple elements                               | `s.update([20, 30])`        |
| `remove()`               | Removes an element (Error if not found)              | `s.remove(10)`              |
| `discard()`              | Removes an element (No error if not found)           | `s.discard(10)`             |
| `pop()`                  | Removes and returns a random element                 | `s.pop()`                   |
| `clear()`                | Removes all elements                                 | `s.clear()`                 |
| `copy()`                 | Returns a copy of the set                            | `s.copy()`                  |
| `union()`                | Combines two sets                                    | `a.union(b)`                |
| `intersection()`         | Returns common elements                              | `a.intersection(b)`         |
| `difference()`           | Returns elements in first set only                   | `a.difference(b)`           |
| `symmetric_difference()` | Returns elements that are in either set but not both | `a.symmetric_difference(b)` |
| `issubset()`             | Checks if one set is a subset of another             | `a.issubset(b)`             |
| `issuperset()`           | Checks if one set is a superset of another           | `a.issuperset(b)`           |
| `isdisjoint()`           | Checks if two sets have no common elements           | `a.isdisjoint(b)`           |

"""

# Operations On Sets
"""
| Operation            | Operator | Method                   | Example           |
| -------------------- | -------- | ------------------------ | ----------------- |
| Union                | `\|`     | `union()`                | `A \| B`          |
| Intersection         | `&`      | `intersection()`         | `A & B`           |
| Difference           | `-`      | `difference()`           | `A - B`           |
| Symmetric Difference | `^`      | `symmetric_difference()` | `A ^ B`           |
| Subset               | `<=`     | `issubset()`             | `A <= B`          |
| Superset             | `>=`     | `issuperset()`           | `A >= B`          |
| Disjoint             | —        | `isdisjoint()`           | `A.isdisjoint(B)` |

"""