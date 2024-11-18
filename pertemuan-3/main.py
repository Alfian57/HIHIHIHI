import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)


class DepositError(Exception):
    pass


class BankAccount:
    def __init__(self, nik, pemilik, saldo):
        self.pemilik = pemilik

        self._no_rekening = "12345678"
        self._saldo = saldo

        self.__nik = nik

    def get_saldo(self):
        return self._saldo

    def deposit(self, nominal):
        if nominal < 10000:
            raise DepositError("Maaf, jumlah deposit minimal 10.000")
        elif nominal > 1000000:
            raise DepositError("Maaf, jumlah deposit maksimal 1.000.000")
        else:
            self._saldo += nominal
            print(f"\nBerhasil deposit sebesar {nominal}")
            print(f"Saldo sekarang {self._saldo}")

    def tarik(self, nominal):
        if nominal < 10000:
            print("\nMaaf, jumlah penarikan minimal 10.000")
        elif nominal > 1000000:
            print("\nMaaf, jumlah penarikan maksimal 1.000.000")
        elif nominal > self._saldo:
            print("\nMaaf, saldo tidak mencukupi")
        else:
            self._saldo -= nominal
            print(f"\nBerhasil penarikan sebesar {nominal}")
            print(f"Saldo sekarang {self._saldo}")

    def info(self):
        print(f"\nPemilik\t\t: {self.pemilik}")
        print(f"No Rekening\t: {self._no_rekening}")
        print(f"Saldo\t\t: {self._saldo}")
        print(f"NIK\t\t: {self.__nik}")


rekening = BankAccount("1234567891", "Alfian", 50000)
while True:
    print("\nMenu Utama")
    print("1. Check Saldo")
    print("2. Deposit")
    print("3. Penarikan")
    print("4. Info Rekening")
    print("5. Keluar")

    menu = input("Pilih menu[1-5] : ")

    if menu == "1":
        print(f"Saldo\t: {rekening.get_saldo()}")

    elif menu == "2":
        try:
            nominal = int(input("Masukan jumlah deposit: "))
            rekening.deposit(nominal)
        except DepositError as e:
            print(e)
            logging.error(e)
        except ValueError:
            print("\n=================")
            print("Input Harus Angka")
            print("=================")

    elif menu == "3":
        try:
            nominal = int(input("Masukan jumlah penarikan: "))
            rekening.tarik(nominal)
        except ValueError:
            print("\n=================")
            print("Input Harus Angka")
            print("=================")

    elif menu == "4":
        rekening.info()

    elif menu == "5":
        break

    else:
        print("\n===============")
        print("MENU TIDAK ADA")
        print("===============")
