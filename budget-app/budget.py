class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': 0 - amount, 'description': description})
        return True

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']

        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        string = ''
        first_line = (30 - len(self.name))//2 * '*'
        string = first_line + self.name + first_line + '\n'
        for transaction in self.ledger:
            next_line = '' 
            description = transaction['description']
            if len(description) >= 23:
                next_line = description[0:23]
            else:
                next_line = description + (" " * (23 - len(description)))

            amount = transaction['amount']
            amount = f'{amount:.2f}'
            if len(amount) >= 7:
                next_line += amount[0:7]
            else:
                next_line += " " * (7 - len(amount))
                next_line += amount

            next_line += '\n'
            string += next_line

        string += f'Total: {self.get_balance():.2f}'
        return string

            


def create_spend_chart(categories):
    chart = 'Percentage spent by category' 
    spent_total = 0
    categories_and_amounts = {}


    for category in categories:
        spent = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                spent += -transaction['amount']

        categories_and_amounts.update({category.name: spent})
        spent_total += spent
        bar_chart_strings = ['100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ', ' 40| ', ' 30| ', ' 20| ', ' 10| ', '  0| ', '    -']

    name_lengh = 0
    for category in categories_and_amounts.keys():
        if name_lengh < len(category):
            name_lengh = len(category)

    while name_lengh >= 1:
        bar_chart_strings.append('     ')
        name_lengh -= 1

    for category, amount in categories_and_amounts.items():
        percentage = amount * 100 / spent_total // 10
        empty_places = 10 - percentage
        percentage += 1
        index = 0
        name_len = len(category)

        for bar_chart_string in bar_chart_strings:
            if empty_places > 0:
                bar_chart_strings[index] += "   "
                empty_places -= 1
                index += 1
                continue

            if percentage > 0:
                bar_chart_strings[index] += "o  "
                percentage -= 1
                index += 1
                continue

            if index == 11:
                bar_chart_strings[index] += "---"
                index += 1
                continue

            if name_len > 0:
                bar_chart_strings[index] += f'{category[(index - 12)]}  '
                name_len -= 1
                index += 1
                continue

            bar_chart_strings[index] += "   "
            index += 1

    for string in bar_chart_strings:
        chart += '\n' + string

    return chart