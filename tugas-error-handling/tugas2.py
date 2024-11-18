class BankAccount:
    def __init__(self, account_id, name, initial_balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, name, initial_balance=0):
        self.accounts[account_id] = BankAccount(account_id, name, initial_balance)

    def access_account(self, account_id):
        return self.accounts[account_id]

    def list_accounts(self):
        for acc_id, acc in self.accounts.items():
            print(
                f"Account ID: {acc_id}, Name: {acc.name}, Balance: {acc.check_balance()}"
            )

    def get_account_attribute(self, account_id, attr):
        account = self.accounts[account_id]
        return getattr(account, attr)


# Triggering Errors

bank = BankSystem()
bank.create_account("123", "Alice", 1000)

# Trigger KeyError (akses akun yang tidak ada)
try:
    account_non_existent = bank.access_account("999")  # KeyError
except KeyError as e:
    print(f"KeyError: {e}")

# Trigger TypeError (tipe tidak valid untuk deposit/withdraw)
account_alice = bank.access_account("123")
try:
    account_alice.deposit("500")  # TypeError: menambahkan string ke balance
except TypeError as e:
    print(f"TypeError: {e}")

try:
    account_alice.withdraw([100])  # TypeError: menarik list dari balance
except TypeError as e:
    print(f"TypeError: {e}")

# Trigger ValueError (jumlah deposit/withdraw negatif)
try:
    account_alice.deposit(
        -500
    )  # ValueError: Python won't automatically raise this, but we'll demonstrate
    print(f"Balance after invalid deposit: {account_alice.check_balance()}")
except ValueError as e:
    print(f"ValueError: {e}")

# Trigger IndexError (akses indeks di luar jangkauan)
try:
    sample_list = [1, 2, 3]
    print(sample_list[5])  # IndexError: index list di luar jangkauan
except IndexError as e:
    print(f"IndexError: {e}")

# Trigger AttributeError (akses atribut yang tidak ada)
try:
    bank.get_account_attribute("123", "non_existent_attr")  # AttributeError
except AttributeError as e:
    print(f"AttributeError: {e}")
