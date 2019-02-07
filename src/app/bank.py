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

    def add_transaction(self, *, sender, recipient, subject, amount):
        # check if sender/recipient account number exists
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        # check if sender/recipient account number matches with sender/recipient
        assert self.accounts[sender.number] == sender, 'Sender account does not match!'
        assert self.accounts[recipient.number] == recipient, 'Recipient account does not match!'

        self.accounts[sender.number].subtract_from_balance(amount)
        self.accounts[recipient.number].add_to_balance(amount)
        transaction = app.Transaction(
            sender=sender.number,
            recipient=recipient.number,
            subject=subject,
            amount=amount)
        self.transactions.append(transaction)
        return transaction
