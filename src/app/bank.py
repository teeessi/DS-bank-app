class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def _get_account_numbers(self):
        # return a number list of all account numbers in self.accounts
        return [account['number'] for account in self.accounts]

    def open_account(self, account):
        assert account['number'] not in self._get_account_numbers(), \
            'Account number ' + str(account['number']) + ' already taken!'
        account['balance'] = 0
        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, 'Amount has to be greater than 0'

        # check account existence
        # if we can rely on account numbers, the following would be sufficient...
        _account_numbers = self._get_account_numbers()
        # assert sender['number'] in _account_numbers, 'Sender has no account yet!'
        # assert recipient['number'] in _account_numbers, 'Recipient has no account yet!'

        # ...but we want to make sure all data matches
        assert sender in self.accounts, 'Sender has no account yet!'
        assert recipient in self.accounts, 'Recipient has no account yet!'

        _transaction = {
            'sender': sender,
            'recipient': recipient,
            'subject': subject,
            'amount': amount,
        }
        self.transactions.append(_transaction)

        # self.accounts[_account_numbers.index(sender('number'))]['balance'] = ...and so on...

        return _transaction
