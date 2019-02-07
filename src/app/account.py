import app


class Account:
    def __init__(self, *, firstname, lastname, number, balance=0.):
        assert isinstance(number, int), 'Number needs to be an integer'
        assert isinstance(balance, float), 'Balance needs to be a float'
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

    def info(self):
        # return formatted account info
        # 'Number 1: Albert Einstein - 100.0 €'
        template = 'Number {number}: {firstname} {lastname} - {balance} €'
        return template.format(
            number=self.number,
            firstname=self.firstname,
            lastname=self.lastname,
            balance=self.balance,
        )

    def has_funds_for(self, amount):
        # check funds for amount, return boolean
        return self.balance >= amount

    def add_to_balance(self, amount):
        assert app.is_positive(amount), 'Amount needs to be greater than 0'
        self.balance += amount

    def subtract_from_balance(self, amount):
        assert app.is_positive(amount), 'Amount needs to be greater than 0'
        assert self.has_funds_for(amount), 'Account has not enough funds'
        self.balance -= amount
