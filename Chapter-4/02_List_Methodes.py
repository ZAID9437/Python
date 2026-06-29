frinds = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(frinds)

# Adding an element to the end of the list
print("Adding an element to the end of the list")
frinds.append("Zaid Mansuri")
print(frinds)


num = [1,34,62,2,6,11,3,5,7,9,0]
print(num)

# Inserting an element at a specific index
print("Inserting an element at a specific index")
num.insert(2, 100)
print(num)

# Popping an element from the list
print("Popping an element from the list")
num.pop(5)
print(num.pop(5))  # Popping the element at index 4
print(num)

# Removing an element from the list
print("Removing an element from the list")
num.remove(62)
print(num)

# Sorting the list
print("Sorting the list")
num.sort()
print(num)

# Reversing the list
print("Reversing the list")
num.reverse()
print(num)


"""
| No. | List Method | Description                                                         |
| --- | ----------- | ------------------------------------------------------------------- |
| 1   | `append()`  | Adds an element to the end of the list.                             |
| 2   | `extend()`  | Adds all elements of another iterable to the list.                  |
| 3   | `insert()`  | Inserts an element at a specified position.                         |
| 4   | `remove()`  | Removes the first occurrence of a specified value.                  |
| 5   | `pop()`     | Removes and returns the element at the given index (default: last). |
| 6   | `clear()`   | Removes all elements from the list.                                 |
| 7   | `index()`   | Returns the index of the first occurrence of a value.               |
| 8   | `count()`   | Returns the number of times a value appears in the list.            |
| 9   | `sort()`    | Sorts the list in ascending order (by default).                     |
| 10  | `reverse()` | Reverses the order of the list.                                     |
| 11  | `copy()`    | Returns a shallow copy of the list.                                 |


numbers = [10, 20, 30]

numbers.append(40)          # [10, 20, 30, 40]
numbers.extend([50, 60])    # [10, 20, 30, 40, 50, 60]
numbers.insert(1, 15)        # [10, 15, 20, 30, 40, 50, 60]
numbers.remove(30)           # Removes 30
numbers.pop()                # Removes last element
numbers.clear()              # []


Quick List of Methods
1. append()
2. extend()
3. insert()
4. remove()
5. pop()
6. clear()
7. index()
8. count()
9. sort()
10. reverse()
11. copy()
"""