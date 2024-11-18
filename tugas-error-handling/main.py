class BankAccount:
    def __init__(self, account_id, name, initial_balance=0):
        if not isinstance(account_id, str) or not isinstance(name, str):
            raise TypeError("Account ID dan Name harus berupa string")
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance harus berupa angka")
        if initial_balance < 0:
            raise ValueError("Initial balance tidak boleh negatif")

        self.account_id = account_id
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Angka deposit harus lebih besar dari nol")
            self.balance += amount
        except TypeError:
            print("TypeError: Amount harus berupa angka")
        except ValueError as e:
            print(f"ValueError: {e}")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Dana tidak mencukupi untuk penarikan")
            if amount <= 0:
                raise ValueError("Jumlah penarikan harus lebih besar dari nol")
            self.balance -= amount
        except TypeError:
            print("TypeError: Amount harus berupa angka")
        except ValueError as e:
            print(f"ValueError: {e}")

    def check_balance(self):
        return self.balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, name, initial_balance=0):
        try:
            if account_id in self.accounts:
                raise KeyError(f"Account dengan ID '{account_id}' sudah ada")
            self.accounts[account_id] = BankAccount(account_id, name, initial_balance)
        except KeyError as e:
            print(f"KeyError: {e}")
        except TypeError:
            print("TypeError: Tipe input tidak valid untuk pembuatan akun")
        except ValueError as e:
            print(f"ValueError: {e}")

    def access_account(self, account_id):
        try:
            return self.accounts[account_id]
        except KeyError:
            print(f"KeyError: Account dengan ID '{account_id}' tidak ditemukan")

    def list_accounts(self):
        try:
            if len(self.accounts) == 0:
                raise IndexError("Tidak ada akun dalam sistem")
            for acc_id, acc in self.accounts.items():
                print(
                    f"Account ID: {acc_id}, Name: {acc.name}, Balance: {acc.check_balance()}"
                )
        except IndexError as e:
            print(f"IndexError: {e}")

    def get_account_attribute(self, account_id, attr):
        try:
            account = self.accounts[account_id]
            return getattr(account, attr)
        except AttributeError:
            print(f"AttributeError: '{attr}' atribut tidak ditemukan di BankAccount")
        except KeyError:
            print(f"KeyError: Account dengan ID '{account_id}' tidak ditemukan")


bank = BankSystem()

# Contoh KeyError
bank.create_account("123", "Alice", 1000)  # Pembuatan akun berhasil
bank.create_account("123", "Alice", 1000)  # KeyError: Akun duplikat

# Contoh TypeError dan ValueError
bank.create_account(123, "Bob", -500)  # TypeError: account_id harus berupa string
bank.create_account("124", "Bob", -500)  # ValueError: Saldo negatif

# Mengakses akun yang tidak ada (KeyError)
account = bank.access_account("999")  # KeyError: Akun tidak ditemukan

# Melakukan transaksi dengan TypeError dan ValueError
account_alice = bank.access_account("123")
if account_alice:
    account_alice.deposit(-100)  # ValueError: Jumlah deposit negatif
    account_alice.deposit("500")  # TypeError: Jumlah bukan numerik
    account_alice.withdraw(2000)  # ValueError: Dana tidak mencukupi
else:
    print("Akun '123' tidak ditemukan, tidak dapat melakukan transaksi")

# Mendaftar akun (IndexError)
bank.list_accounts()  # Berhasil mendaftar akun

# IndexError: Mencoba mendaftar akun saat tidak ada akun
empty_bank = BankSystem()
empty_bank.list_accounts()  # IndexError: Tidak ada akun dalam sistem

# Contoh AttributeError
bank.get_account_attribute(
    "123", "non_existent_attr"
)  # AttributeError: Atribut tidak valid
