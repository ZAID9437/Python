# 3. Check that a tuple type cannot be changed in python
a = (34, 234, "Zaid", 0, 0, 9)
a[2] = "Mansuri"  # This will raise a TypeError because tuples are immutable