import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
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

    def tarik(self, nominal):
        if nominal < 10000:
            raise ValueError("Maaf, jumlah penarikan minimal 10.000")
        elif nominal > 1000000:
            raise ValueError("Maaf, jumlah penarikan maksimal 1.000.000")
        elif nominal > self._saldo:
            raise ValueError("Maaf, saldo tidak mencukupi")
        else:
            self._saldo -= nominal

    def info(self):
        return f"Pemilik: {self.pemilik}\nNo Rekening: {self._no_rekening}\nSaldo: {self._saldo}\nNIK: {self.__nik}"


class BankApp:
    def __init__(self, root):
        self.rekening = BankAccount("1234567891", "Alfian", 50000)
        self.root = root
        self.root.title("Bank Account Management")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.configure("TLabel", padding=6, background="#eee")

        self.main_frame = ttk.Frame(root, padding="10 10 10 10")
        self.main_frame.pack(pady=20)

        self.saldo_label = ttk.Label(self.main_frame, text="Saldo: 0")
        self.saldo_label.pack()

        self.deposit_button = ttk.Button(
            self.main_frame, text="Deposit", command=self.deposit
        )
        self.deposit_button.pack(pady=5)

        self.withdraw_button = ttk.Button(
            self.main_frame, text="Withdraw", command=self.withdraw
        )
        self.withdraw_button.pack(pady=5)

        self.info_button = ttk.Button(self.main_frame, text="Info", command=self.info)
        self.info_button.pack(pady=5)

        self.update_saldo()

    def update_saldo(self):
        self.saldo_label.config(text=f"Saldo: {self.rekening.get_saldo()}")

    def deposit(self):
        nominal = self.get_nominal("Masukan jumlah deposit:")
        if nominal is not None:
            try:
                self.rekening.deposit(nominal)
                self.update_saldo()
                messagebox.showinfo("Success", f"Berhasil deposit sebesar {nominal}")
            except DepositError as e:
                messagebox.showerror("Error", str(e))
                logging.error(e)

    def withdraw(self):
        nominal = self.get_nominal("Masukan jumlah penarikan:")
        if nominal is not None:
            try:
                self.rekening.tarik(nominal)
                self.update_saldo()
                messagebox.showinfo("Success", f"Berhasil penarikan sebesar {nominal}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def info(self):
        info = self.rekening.info()
        messagebox.showinfo("Info Rekening", info)

    def get_nominal(self, prompt):
        nominal_str = simpledialog.askstring("Input", prompt)
        try:
            if nominal_str is not None:
                return int(nominal_str)
            return None
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Input harus angka")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
