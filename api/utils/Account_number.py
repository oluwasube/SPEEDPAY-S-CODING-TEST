import random


def generate_account_number():
    # Set to store used account numbers
    used_account_numbers = set()

    while True:

        account_number = random.randint(100000, 999999)

        if account_number not in used_account_numbers:
            used_account_numbers.add(account_number)
            return account_number
