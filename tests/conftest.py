import pytest

from budget_app.budget import *

@pytest.fixture
def category():
    return Category('Category name')

@pytest.fixture
def category1():
    return Category('Category1 name')