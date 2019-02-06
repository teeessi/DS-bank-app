class Transaction:
    def __init__(self, *, sender, recipient, subject, amount):
        assert isinstance(sender, int), 'Sender needs to be an integer'
        assert isinstance(recipient, int), 'Recipient needs to be an integer'
        assert isinstance(amount, float), 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount

    def info(self):
        # return formatted transaction info
        # 'From 1 to 2: Test transaction - 10.0 €'
        return 'From {} to {}: {} - {} €'.format(
            self.sender,
            self.recipient,
            self.subject,
            self.amount,
        )
