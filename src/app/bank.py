class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def _get_account_numbers(self):
        # return a number list of all account numbers in self.accounts
        return [account['number'] for account in self.accounts]

    def open_account(self, account):
        # enter account in accounts list, return account dictionary including added elements
        assert account['number'] not in self._get_account_numbers(), \
            'Account number {} already taken!'.format(account['number'])
        account['balance'] = 0.
        self.accounts.append(account)
        return account
        # structure of account
        # {
        #     'number': int,
        #     'firstname': string,
        #     'lastname': string,
        #     'balance': float
        # }

    def add_transaction(self, *, sender, recipient, subject, amount):
        # enter transaction in transactions list, return transaction as dictionary
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

    def _print_account(self, account):
        # return formatted account string
        return ('Konto {}, {} {}, Saldo {}'.format(
            account['number'],
            account['firstname'],
            account['lastname'],
            account['balance'],
        ))

    def info(self):
        # print all data in bank object
        print('Bank: {}'.format(self.name))
        print()

        print('Konten:')
        for index, account in enumerate(self.accounts):
            print('{}: {}'.format(
                index,
                self._print_account(account)
             ))
        print()

        print('Transaktionen:')
        for index, transaction in enumerate(self.transactions):
            print('{}: Verwendungszweck "{}", Betrag {}\n\tSender:    {}\n\tEmpfänger: {}'.format(
                index,
                transaction['subject'],
                transaction['amount'],
                self._print_account(transaction['sender']),
                self._print_account(transaction['recipient']),
            ))
