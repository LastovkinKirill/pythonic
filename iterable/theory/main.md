# **Key Differences & Comparisons**

- **All generators are iterators**
- **All iterators are iterables**
- **BUT not all iterables are iterators**

So: **Generators ⊂ Iterators ⊂ Iterables**

## **Hierarchy Visualization:**

```
      Iterables (implements __iter__)
          / \
         /   \
        /     \
    Iterators   Non-iterator Iterables
   (implements  (like lists, tuples,
    __next__)    strings, dicts, etc.)
       |
       |
    Generators
   (function with yield)
```

### **Iterable vs Iterator:**

| Iterable                       | Iterator                                 |
|--------------------------------|------------------------------------------|
| Implements `__iter__()`        | Implements `__iter__()` and `__next__()` |
| Can be iterated multiple times | Can be iterated only once                |
| All items in memory            | Items generated on-demand                |
| Examples: list, tuple, dict    | Examples: zip(), map(), file objects     |

### **Iterator vs Generator:**

| Iterator                           | Generator                   |
|------------------------------------|-----------------------------|
| Class-based implementation         | Function-based with `yield` |
| Manual `__next__()` implementation | Automatic `__next__()`      |
| More boilerplate code              | Concise syntax              |
| Can be complex to write            | Easier to write and read    |

---

## **Key Insight:**

- **Iterables** are **producers of iterators** (when you call `iter()` on them)
- **Iterators** are **consumers of values** (when you call `next()` on them)
- **Generators** are **factory functions for iterators** (using `yield`)