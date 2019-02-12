import pandas as pd


class Bank:
    # template credits to mar-volk
    def __init__(self, name):
        self.name = name

        self.accounts = pd.DataFrame(columns=[
            'id',
            'firstname',
            'lastname',
            'balance'
        ])
        self.transactions = pd.DataFrame(columns=[
            'id',
            'sender_id',
            'recipient_id',
            'amount',
            'subject',
            'category',
            'timestamp'
        ])

    def open_account(self, *, account_id, firstname, lastname, balance=0.0):
        assert account_id not in self.accounts['id'].values, 'Account number {} already taken!'.format(account_id)

        account = {
            'id': account_id,
            'firstname': firstname,
            'lastname': lastname,
            'balance': balance
        }
        self.accounts = self.accounts.append(account, ignore_index=True)
        return self.accounts

    def add_transaction(self, *, transaction_id, sender_id, recipient_id, subject, amount, category, timestamp):
        assert amount > 0, 'Amount needs to be greater than 0'
        # sender and recipient accounts exist?
        assert sender_id in self.accounts['id'].values, 'Sender has no account yet!'
        assert recipient_id in self.accounts['id'].values, 'Recipient has no account yet!'

        transaction = {
            'id': transaction_id,
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'amount': amount,
            'subject': subject,
            'category': category,
            'timestamp': timestamp
        }
        self.transactions = self.transactions.append(transaction, ignore_index=True)
        return self.transactions
