class HashTable:
    """A hash table implementation with collision handling via nested dictionaries."""
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        """Calculate hash value using weighted sum of character codes."""
        return sum(ord(ch) * (i + 1) for i, ch in enumerate(string)) 

    def add(self, key, value):
        """Add or update a key-value pair."""
        hashed = self.hash(key)
        if hashed in self.collection:
            self.collection[hashed].update({key: value})
        else:
            self.collection.update({hashed: {key: value}})


    def remove(self, key):
        """Remove a key-value pair. Does nothing if key doesn't exist."""
        hashed = self.hash(key)
        if hashed in self.collection:
            if key in self.collection[hashed]:
                self.collection[hashed].pop(key)
                if not self.collection[hashed]:
                    del self.collection[hashed]

    def lookup(self, key):
        """Return value for key, or None if not found."""
        hashed = self.hash(key)
        if hashed in self.collection:
            if key in self.collection[hashed].keys():
                return self.collection[hashed][key]
        else:
            return None
        
    def __str__(self):
        """Return string representation of the hash table."""
        result = []
        for inner_dict in self.collection.values():
            for key, value in inner_dict.items():
                result.append(f"'{key}': {value}")
        return "{" + ", ".join(result) + "}"
    
    def __contains__(self, key):
        """Enable 'key in hashtable' syntax."""
        return self.lookup(key) is not None