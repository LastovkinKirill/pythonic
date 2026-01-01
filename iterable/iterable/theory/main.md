# Iterables

### **What is an Iterable?**

- Any Python object capable of returning its elements **one at a time**
- Can be looped over using `for` loops
- Must implement either:
    - `__iter__(self)` method (must return an iterator (an object with __next__() method))
    - `__getitem__(self, index):` method (sequence protocol)
      - Automatic iterator creation: When Python can't find __iter__(), it falls back to calling __getitem__() with sequential integers (0, 1, 2, ...)

### **Key Characteristics:**

- Can be iterated over multiple times
- Store all elements in memory (usually)
