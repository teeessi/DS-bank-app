from .account import Account
from .transaction import Transaction
from .bank import Bank


def is_positive(number):
    return number > 0


__all__ = ['Account', 'Transaction', 'Bank']
