import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        assert isinstance(account, app.Account), 'Account should be an app.Account'
        assert account.number not in self.accounts, 'Account number {} already taken!'.format(account.number)
        self.accounts[account.number] = account
        return account

    def _account_number_exists(self, account_number):
        return account_number in self.accounts

    def _account_matches(self, account):
        return self.accounts[account.number] == account

    def add_transaction(self, *, sender, recipient, subject, amount):
        # check if sender/recipient account number exists
        assert self._account_number_exists(sender.number), 'Sender has no account yet!'
        assert self._account_number_exists(recipient.number), 'Recipient has no account yet!'
        # check if sender/recipient account number matches with sender/recipient account
        assert self._account_matches(sender), 'Sender account does not match!'
        assert self._account_matches(recipient), 'Recipient account does not match!'

        self.accounts[sender.number].subtract_from_balance(amount)
        self.accounts[recipient.number].add_to_balance(amount)
        transaction = app.Transaction(
            sender=sender.number,
            recipient=recipient.number,
            subject=subject,
            amount=amount)
        self.transactions.append(transaction)
        return transaction
