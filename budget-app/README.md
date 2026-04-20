# Budget App

A Python class for managing personal finances — deposits, withdrawals, transfers between categories, and a spending chart.

## Features
- Deposit and withdraw money with descriptions
- Transfer funds between budget categories
- Check balance and available funds
- Generate a spending percentage chart for multiple categories
- Unit tests (pytest) are in progress — will be added by the end of May.

## Example
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")
print(food)

clothes = Category("Clothes")
clothes.deposit(500)
food.transfer(50, clothes)

chart = create_spend_chart([food, clothes])
print(chart)

