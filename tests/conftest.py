import pytest

from budget_app.budget import Category
from hashtable.hashtable import HashTable

@pytest.fixture
def category():
    return Category('Category name')

@pytest.fixture
def category1():
    return Category('Category1 name')

@pytest.fixture
def hash_table():
    return HashTable()