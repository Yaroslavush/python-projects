from hashtable.hashtable import HashTable

def test_add_and_lookup(hash_table):
    hash_table.add("key1", "arg1")
    hash_table.add("key2", "arg2")
    hash_table.add("key2", "arg3")

    assert hash_table.lookup("key1") == "arg1"
    assert hash_table.lookup("key2") == "arg3"

def test_remove(hash_table):
    hash_table.add("key1", "arg1")
    hash_table.add("key2", "arg2")
    hash_table.remove("key1")
    hash_table.remove("key2")
    hash_table.remove("key2")

    assert hash_table.lookup("key1") is None
    assert hash_table.lookup("key2") is None

def test_contains(hash_table):
    hash_table.add("key1", "arg1")

    assert not "key2" in hash_table
    assert "key1" in hash_table


