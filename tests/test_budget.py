import pytest

from budget_app.budget import *

def test_deposit(category):
    category.deposit(30, 'description')

    assert category.ledger[-1]['amount'] == 30
    assert category.ledger[-1]['description'] == 'description'

def test_get_balance(category):
    category.deposit(100)
    category.withdraw(30)

    assert category.get_balance() == 70

@pytest.mark.parametrize("transfer_amount, expected_balance, expected_result", [
    (20, 10, True), 
    (30, 0, True), 
    (40, 30, False)
])
def test_withdraw(category, transfer_amount, expected_balance, expected_result):
    category.deposit(30)

    assert category.withdraw(transfer_amount) == expected_result
    assert category.get_balance() == expected_balance

@pytest.mark.parametrize("transfer_amount, expected_sender_balance, expected_receiver_balance, expected_result", [
    (20, 10, 20, True), 
    (30, 0, 30, True), 
    (40, 30, 0, False)
])
def test_transfer(category, category1, transfer_amount, expected_sender_balance, expected_receiver_balance, expected_result):
    category.deposit(30)

    assert category.transfer(transfer_amount, category1) == expected_result
    assert category.get_balance() == expected_sender_balance
    assert category1.get_balance() == expected_receiver_balance

def test_create_spend_chart_structure(category, category1):
    category.deposit(100)
    category.withdraw(30)
    category.transfer(20, category1)

    result = create_spend_chart([category, category1])

    for i in range(100, -1, -10):
        assert f"{i:>3}|" in result or f" {i:>2}|" in result
    assert "o" in result

