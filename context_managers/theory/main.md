# Python Context Managers

## What Is a Context Manager?

A **context manager** is an object that:

- Sets up a context (allocates resources)
- Tears it down (releases resources)
- Guarantees cleanup **even if an exception occurs**

In Python terms:

> A context manager is an object that defines `__enter__` and `__exit__` to guarantee **deterministic setup and cleanup
of resources** around a block of code.

---

## Why Use Context Managers?

Context managers are used to:

- Prevent resource leaks
- Write cleaner, safer code
- Ensure exception safety
- Enable composable and reusable resource management

---

## How It Works

Context managers follow the **Context Manager Protocol**.

A class is a context manager if it implements:

```python
__enter__(self) -> Optional[Any]
__exit__(self, exc_type, exc_value, traceback) -> Optional[bool]
```

| __exit__ returns | Result               |
|------------------|----------------------|
| True             | Exception suppressed |
| False or None    | Exception re-raised  |

## Other

Common Built-in Context Managers:

| Context Manager          | Purpose         |
|--------------------------|-----------------|
| open()                   | File handling   |
| threading.Lock()         | Synchronization |
| sqlite3.connect()        | DB connection   |
| tempfile.TemporaryFile() | Temp files      |

