import datetime, calendar
import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = {}

    def open_account(self, account):
        assert isinstance(account, app.Account), 'Account should be an app.Account'
        assert account.number not in self.accounts, 'Account number {} already taken!'.format(account.number)
        account.bank = self
        self.accounts[account.number] = account
        return account

    def _account_number_exists(self, account_number):
        return account_number in self.accounts

    def _account_matches(self, account):
        return self.accounts[account.number] == account

    def add_transaction(self, *, sender, recipient, subject, amount, date=None, category=None):
        # check if sender/recipient account number exists
        assert self._account_number_exists(sender.number), 'Sender has no account yet!'
        assert self._account_number_exists(recipient.number), 'Recipient has no account yet!'
        # check if sender/recipient account number matches with sender/recipient account
        assert self._account_matches(sender), 'Sender account does not match!'
        assert self._account_matches(recipient), 'Recipient account does not match!'

        # assign current date if no date is given
        if not date:
            utcdatenow = datetime.datetime.utcnow()                 # UTC datetime
            date = calendar.timegm(utcdatenow.timetuple())  # UTC timestamp

        # assign transaction_id
        # 1 if dict is empty, else highest transaction_id + 1
        transaction_id = 1 if not len(self.transactions) else max(self.transactions.keys()) + 1

        self.accounts[sender.number].subtract_from_balance(amount)
        self.accounts[recipient.number].add_to_balance(amount)
        transaction = app.Transaction(
            transaction_id=transaction_id,
            sender=sender.number,
            recipient=recipient.number,
            subject=subject,
            amount=amount,
            date=date,
            category=category,
        )
        self.transactions[transaction_id] = transaction
        return transaction

    def info(self):
        print('Bank: {bank}'.format(bank=self.name))

        print('\nAccounts:')
        for account in self.accounts.values():
            print(account.info())

        print('\nTransactions:')
        for transaction in self.transactions.values():
            print(transaction.info())
