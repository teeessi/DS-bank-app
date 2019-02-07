import datetime
import utils


class Transaction:
    def __init__(self, *, transaction_id, sender, recipient, subject, amount, date, category):
        assert isinstance(sender, int), 'Sender needs to be an integer'
        assert isinstance(recipient, int), 'Recipient needs to be an integer'
        assert isinstance(amount, float), 'Amount needs to be a float'
        assert utils.is_positive(amount), 'Amount needs to be greater than 0'
        assert isinstance(date, (int, float)), 'Date must be passed as UTC timestamp!'
        self.transaction_id = transaction_id
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount
        self.date = date
        self.category = category

    def add_category(self, category):
        self.category = category

    def info(self):
        # return formatted transaction info
        # 'From 1 to 2: Test transaction - 10.0 €'
        template = 'Id {transaction_id}: Date {date} - From {sender} to {recipient}: {subject} - {amount} €'
        if self.category:
            template += ' - Category: {category}'

        # format Date from UTC timestamp
        date = datetime.datetime.fromtimestamp(self.date).strftime('%Y-%m-%d %H:%M:%S')

        return template.format(
            transaction_id=self.transaction_id,
            date=date,
            sender=self.sender,
            recipient=self.recipient,
            subject=self.subject,
            amount=self.amount,
            category=self.category,
        )
