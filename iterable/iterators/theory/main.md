# Iterators

### **What is an Iterator?**
- An object with state that remembers where it is during iteration
- Must implement:
  - `__iter__()` → returns self [do not always] it should return object with __next__() method
  - `__next__()` → returns next item or raises `StopIteration`

### **Key Characteristics:**
- **Exhaustible**: Can only be iterated over once
- **Lazy evaluation**: Computes next value on demand
- **Stateful**: Remembers position
- **One-way**: Can only move forward


