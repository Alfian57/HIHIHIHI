import tkinter as tk
from tkinter import ttk
from db_config import Database
from tkinter import messagebox


class InventoryBarang:

    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Barang")
        self.db = Database()

        self.form_frame = tk.Frame(self.root, padx=10, pady=10)
        self.form_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.form_frame, text="Nama Barang").grid(row=0, column=0, sticky="W")
        self.nama_barang = tk.Entry(self.form_frame)
        self.nama_barang.grid(row=0, column=1)

        tk.Label(self.form_frame, text="Jumlah").grid(row=1, column=0, sticky="W")
        self.jumlah_barang = tk.Entry(self.form_frame)
        self.jumlah_barang.grid(row=1, column=1)

        tk.Label(self.form_frame, text="Harga").grid(row=2, column=0, sticky="W")
        self.harga_barang = tk.Entry(self.form_frame)
        self.harga_barang.grid(row=2, column=1)

        self.button_frame = tk.Button(
            self.form_frame, text="Tambah Barang", command=self.add_item
        ).grid(row=3, columnspan=2, pady=10)

        self.table_frame = tk.Frame(self.root, padx=10, pady=10)
        self.table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.table = ttk.Treeview(
            self.table_frame,
            columns=("ID", "Nama Barang", "Jumlah", "Harga"),
            show="headings",
        )
        self.table.heading("ID", text="ID")
        self.table.heading("Nama Barang", text="Nama Barang")
        self.table.heading("Jumlah", text="Jumlah")
        self.table.heading("Harga", text="Harga")
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.root, padx=10, pady=10)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.delete_button = tk.Button(
            self.button_frame, text="Hapus Barang", command=self.delete_item
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.refresh_button = tk.Button(self.button_frame, text="Refresh Data")
        self.refresh_button.pack(side=tk.LEFT, padx=5)

        self.load_items()

    def load_items(self):
        for row in self.table.get_children():
            self.table.delete(row)

        items = self.db.fetchAll("SELECT * FROM items")
        for item in items:
            self.table.insert("", tk.END, values=item)

    def add_item(self):
        nama_barang = self.nama_barang.get()
        jumlah_barang = self.jumlah_barang.get()
        harga_barang = self.harga_barang.get()

        try:
            jumlah = int(jumlah_barang)
            harga = float(harga_barang)
            self.db.execute(
                "INSERT INTO items (name, quantity, price) VALUES (%s, %s, %s)",
                (nama_barang, jumlah, harga),
            )

            messagebox.showinfo("Sukses", "Barang berhasil ditambahkan")
            self.load_items()
        except ValueError:
            messagebox.showerror("Error", "Jumlah dan harga harus berupa angka")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_item(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Pilih barang yang ingin dihapus")
            return

        item_id = self.table.item(selected_item)["values"][0]
        try:
            self.db.execute("DELETE FROM items WHERE id = %s", (item_id,))
            messagebox.showinfo("Sukses", "Barang berhasil dihapus")
            self.load_items()
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    root = tk.Tk()
    app = InventoryBarang(root)
    root.mainloop()


if __name__ == "__main__":
    main()
