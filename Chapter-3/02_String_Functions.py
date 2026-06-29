# 1. len() returns the length of the string.

name = 'Zaid Mansuri'
print("The Lenght Of Number Is Like :- ",len(name))

# 2. endswith() checks if a string ends with given text.

print("The Name is end with this word like ('uri'):-", name.endswith('uri'))
print("The Name is end with this word like ('uri'):-", name.endswith('urii'))

# 3. count() counts total occurrences of a character.

count = name.count('a')
print("The Count Of (a) in my name in how many time:- ",count)

# 4. capitalize() capitalizes the first character.

a = 'zaid mansuri'
print("The My name is First Character should be convert in to capital:- ", a.capitalize())

# 5. find() returns the index of first occurrence.

index = name.find('a')
print("The Find The Character in the name :- ",index)

# 6. replace(old word, new word) replaces the old word with the new word in the string.

replaced = name.replace('Zaid', 'Mansuri')
print("Replace The my Name Zaid To Mansuri:- ",replaced)

"""
| Function       | Description                       | Example                          | Output              |
| -------------- | --------------------------------- | -------------------------------- | ------------------- |
| `len()`        | Returns string length             | `len("Python")`                  | `6`                 |
| `lower()`      | Converts to lowercase             | `"HELLO".lower()`                | `"hello"`           |
| `upper()`      | Converts to uppercase             | `"hello".upper()`                | `"HELLO"`           |
| `title()`      | First letter of each word capital | `"hello world".title()`          | `"Hello World"`     |
| `capitalize()` | First letter capital              | `"python".capitalize()`          | `"Python"`          |
| `swapcase()`   | Swaps upper/lower case            | `"PyThOn".swapcase()`            | `"pYtHoN"`          |
| `strip()`      | Removes spaces from both sides    | `" hello ".strip()`              | `"hello"`           |
| `lstrip()`     | Removes left spaces               | `" hello".lstrip()`              | `"hello"`           |
| `rstrip()`     | Removes right spaces              | `"hello ".rstrip()`              | `"hello"`           |
| `replace()`    | Replaces text                     | `"Hello".replace("H","Y")`       | `"Yello"`           |
| `find()`       | Finds first index                 | `"Python".find("t")`             | `2`                 |
| `index()`      | Finds index (error if not found)  | `"Python".index("o")`            | `4`                 |
| `count()`      | Counts occurrences                | `"banana".count("a")`            | `3`                 |
| `startswith()` | Checks beginning                  | `"Python".startswith("Py")`      | `True`              |
| `endswith()`   | Checks ending                     | `"Python".endswith("on")`        | `True`              |
| `split()`      | Splits into list                  | `"a,b,c".split(",")`             | `['a','b','c']`     |
| `join()`       | Joins list into string            | `"-".join(["a","b","c"])`        | `"a-b-c"`           |
| `isalpha()`    | Only letters                      | `"Python".isalpha()`             | `True`              |
| `isdigit()`    | Only digits                       | `"123".isdigit()`                | `True`              |
| `isalnum()`    | Letters and digits                | `"abc123".isalnum()`             | `True`              |
| `isspace()`    | Only spaces                       | `"   ".isspace()`                | `True`              |
| `islower()`    | All lowercase                     | `"hello".islower()`              | `True`              |
| `isupper()`    | All uppercase                     | `"HELLO".isupper()`              | `True`              |
| `istitle()`    | Title case                        | `"Hello World".istitle()`        | `True`              |
| `center()`     | Centers string                    | `"Python".center(10,"*")`        | `"**Python**"`      |
| `ljust()`      | Left align                        | `"Hi".ljust(5,"-")`              | `"Hi---"`           |
| `rjust()`      | Right align                       | `"Hi".rjust(5,"-")`              | `"---Hi"`           |
| `zfill()`      | Pads with zeros                   | `"25".zfill(5)`                  | `"00025"`           |
| `format()`     | Formats string                    | `"My name is {}".format("Zaid")` | `"My name is Zaid"` |
"""