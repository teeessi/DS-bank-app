class Account:
    def __init__(self, *, firstname, lastname, number, balance = 0.):
        assert isinstance(number, int), 'Number needs to be an integer'
        assert isinstance(balance, float), 'Balance needs to be a float'
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

    def info(self):
        # return formatted account info
        # 'Number 1: Albert Einstein - 100.0 €'
        return 'Number {}: {} {} - {} €'.format(
            self.number,
            self.firstname,
            self.lastname,
            self.balance,
        )

    def has_funds_for(self, amount):
        # check funds for amount, return boolean
        return self.balance >= amount

    def add_to_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        self.balance += amount

    def subtract_from_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        assert self.balance >= amount, 'Account has not enough funds'
        self.balance -= amount
