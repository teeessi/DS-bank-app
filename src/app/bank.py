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
        account['balance'] = 0.
        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, 'Amount has to be greater than 0'

        # check account existence
        assert sender in self.accounts, 'Sender has no account yet!'
        assert recipient in self.accounts, 'Recipient has no account yet!'

        _transaction = {
            'sender': sender,
            'recipient': recipient,
            'subject': subject,
            'amount': amount,
        }
        self.transactions.append(_transaction)

        # _account_numbers = self._get_account_numbers()
        # _sender_account_index = self.accounts[_account_numbers.index(sender('number'))]
        # _recipient_account_index = self.accounts[_account_numbers.index(recipient('number'))]
        # self.accounts[_sender_account_index]('balance') = 0

        return _transaction
