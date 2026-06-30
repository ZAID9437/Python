marks = {
    "Zaid Mansuri": 95,
    "Sahal Patel" : 90,
    "Maaj Nandoliya": 100,
    "Kaif Mansuri" : [20, 25, 45]
}

# print(marks,"\n",type(marks))

# print(marks["Kaif Mansuri"])

# Updates the dictionary with supplied key-value pairs
print("Updates the dictionary with supplied key-value pairs")
print(marks.update({"Zaid Mansuri": 100}))
print(marks)

# Returns the value of the specified keys
print("Returns the value of the specified keys")
print(marks.get("Zaid Mansuri"))

#  Returns a list of (key,value) tuples
print("Returns a list of (key,value) tuples")
print(marks.items())

# Returns a list containing dictionary's keys
print("Returns a list containing dictionary's keys")
print(marks.keys())
print(marks.values())




# GPT Code 
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

print(student.keys())        # dict_keys(['name', 'age', 'course'])
print(student.values())      # dict_values(['Alice', 20, 'Python'])
print(student.items())       # dict_items([('name', 'Alice'), ('age', 20), ('course', 'Python')])

print(student.get("age"))    # 20

student.update({"age": 21})
print(student)               # {'name': 'Alice', 'age': 21, 'course': 'Python'}

student.pop("course")
print(student)               # {'name': 'Alice', 'age': 21}

student.setdefault("city", "New York")
print(student)               # {'name': 'Alice', 'age': 21, 'city': 'New York'}

"""
| Method                     | Description                                                                           | Example                        |
| -------------------------- | ------------------------------------------------------------------------------------- | ------------------------------ |
| `keys()`                   | Returns all keys                                                                      | `d.keys()`                     |
| `values()`                 | Returns all values                                                                    | `d.values()`                   |
| `items()`                  | Returns key-value pairs                                                               | `d.items()`                    |
| `get(key)`                 | Gets the value for a key (returns `None` if not found)                                | `d.get("name")`                |
| `update()`                 | Adds or updates key-value pairs                                                       | `d.update({"age": 25})`        |
| `pop(key)`                 | Removes a key and returns its value                                                   | `d.pop("age")`                 |
| `popitem()`                | Removes and returns the last inserted key-value pair                                  | `d.popitem()`                  |
| `clear()`                  | Removes all items                                                                     | `d.clear()`                    |
| `copy()`                   | Returns a shallow copy                                                                | `d.copy()`                     |
| `setdefault(key, default)` | Returns the value if the key exists; otherwise inserts the key with the default value | `d.setdefault("city", "NY")`   |
| `fromkeys(keys, value)`    | Creates a new dictionary from given keys                                              | `dict.fromkeys(["a", "b"], 0)` |

"""