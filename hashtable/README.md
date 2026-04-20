# Hash Table Implementation

A custom hash table (dictionary) implementation in Python, demonstrating understanding of hash functions, collision handling, and data structures.

## Features

- **Custom hash function** – weighted sum of character codes (position matters)
- **Collision handling** – nested dictionaries store multiple keys with the same hash
- **Core operations** – add, remove, lookup (O(1) average case)
- **Magic methods** – `__str__` and `__contains__` (supports `key in hashtable`)

## Usage Example

```python
from hashtable import HashTable

ht = HashTable()

# Add key-value pairs
ht.add("name", "Yaroslava")
ht.add("city", "Vilnius")

# Lookup values
print(ht.lookup("name"))  # "Yaroslava"

# Check existence
print("city" in ht)       # True

# Remove a key
ht.remove("city")
print(ht.lookup("city"))  # None

# String representation
print(ht)                 # {'name': 'Yaroslava'}