import tkinter as tk
from tkinter import ttk


class InventoryBarang:

    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Barang")

        self.form_frame = tk.Frame(self.root, padx=10, pady=10)
        self.form_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.form_frame, text="Nama Barang").grid(row=0, column=0, sticky="W")
        self.nama_barang = tk.Entry(self.form_frame).grid(row=0, column=1)

        tk.Label(self.form_frame, text="Jumlah").grid(row=1, column=0, sticky="W")
        self.jumlah_barang = tk.Entry(self.form_frame).grid(row=1, column=1)

        tk.Label(self.form_frame, text="Harga").grid(row=2, column=0, sticky="W")
        self.harga_barang = tk.Entry(self.form_frame).grid(row=2, column=1)

        self.button_frame = tk.Button(self.form_frame, text="Tambah Barang").grid(
            row=3, columnspan=2, pady=10
        )

        self.table_frame = tk.Frame(self.root, padx=10, pady=10)
        self.table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.table = ttk.Treeview(
            self.table_frame,
            columns=("ID", "Nama Barang", "Jumlah", "Harga"),
            show="headings",
        )
        self.table.heading("ID", text="ID Barang")
        self.table.heading("Nama Barang", text="Nama Barang")
        self.table.heading("Jumlah", text="Jumlah")
        self.table.heading("Harga", text="Harga")
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.root, padx=10, pady=10)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        self.delete_button = tk.Button(self.button_frame, text="Hapus Barang")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.refresh_button = tk.Button(self.button_frame, text="Refresh Data")
        self.refresh_button.pack(side=tk.LEFT, padx=5)


def main():
    root = tk.Tk()
    app = InventoryBarang(root)
    root.mainloop()


if __name__ == "__main__":
    main()
