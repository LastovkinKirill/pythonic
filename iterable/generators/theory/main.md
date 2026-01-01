# Generators

### **What are Generators?**

- Special type of iterator created using `yield`
- Two types: Generator functions and Generator expressions

### **Control gen lifecycle outside by .throw and .close**

```python
gen.throw(ValueError, "Something went wrong")
gen.close()[gen.throw(GeneratorExit)]
```

### gen.close() method

The `close()` method in generators is used to **terminate the generator prematurely**, causing it to immediately stop
execution and raise a `GeneratorExit` exception internally.

## What `close()` does:

1. **Raises `GeneratorExit`** inside the generator at the point where it's currently suspended
2. **Cleans up resources** if the generator has cleanup code in a `try...finally` block or context manager
3. **Marks the generator as closed** - subsequent calls to `next()` or `send()` will raise `StopIteration`

## Important Notes:

- **`GeneratorExit` is NOT propagated** - it's caught internally by the generator
- **You can catch `GeneratorExit`** to perform cleanup, but you shouldn't yield from the exception handler
- **Already exhausted generators** (that raised `StopIteration`) can still be closed safely
- **`close()` is called automatically** in `for` loops and when generators are garbage collected