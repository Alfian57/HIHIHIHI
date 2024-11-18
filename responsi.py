list_kendaraan = []


class Kendaraan:
    def __init__(self, merk, biaya_sewa_perhari) -> None:
        self.merk = merk
        self.biaya_sewa_perhari = biaya_sewa_perhari

    def biaya_sewa(self, hari):
        return self.biaya_sewa_perhari * hari


class Truk(Kendaraan):
    def biaya_sewa(self, hari):
        return self.biaya_sewa_perhari * hari + (self.biaya_sewa_perhari * hari * 0.15)


class Mobil(Kendaraan):
    def biaya_sewa(self, hari):
        return self.biaya_sewa_perhari * hari + (self.biaya_sewa_perhari * hari * 0.10)


class Motor(Kendaraan):
    pass


def print_menu():
    print("\n== Menu ==")
    print("1. Tambah Kendaraan")
    print("2. Lihat Daftar Kendaraan")
    print("3. Hitung Biaya Sewa")
    print("4. Keluar")


def tambah_kendaraan(jenis, merk, biaya_sewa_perhari):
    if jenis == "mobil":
        kendaraan_baru = Mobil(merk, biaya_sewa_perhari)
        list_kendaraan.append(kendaraan_baru)
    elif jenis == "motor":
        kendaraan_baru = Motor(merk, biaya_sewa_perhari)
        list_kendaraan.append(kendaraan_baru)
    elif jenis == "truk":
        kendaraan_baru = Truk(merk, biaya_sewa_perhari)
        list_kendaraan.append(kendaraan_baru)


def tampilkan_kendaraan():
    global list_kendaraan
    print("\n== Daftar Kendaraan ==")
    for index, kendaraan in enumerate(list_kendaraan):
        print(
            f"{index+1}. {kendaraan.merk}, Biaya per hari: Rp {kendaraan.biaya_sewa_perhari}"
        )


def main():
    while True:
        print_menu()
        input_menu = input("Pilih menu: ")

        if input_menu == "1":
            print("\n== Tambah Kendaraan ==")
            print("1. Mobil")
            print("2. Motor")
            print("3. Truk")
            sub_input_satu = input("Pilih jenis kendaraan (1/2/3): ")

            if sub_input_satu == "1":
                try:
                    merk = input("Masukan merk kendaraan : ")
                    harga_per_hari = int(input("Masukan biaya sewa per hari : "))
                    tambah_kendaraan("mobil", merk, harga_per_hari)

                except ValueError:
                    print("\n========================")
                    print("Masukan harus berupa angka")
                    print("========================")

            elif sub_input_satu == "2":
                try:
                    merk = input("Masukan merk kendaraan : ")
                    harga_per_hari = int(input("Masukan biaya sewa per hari : "))
                    tambah_kendaraan("motor", merk, harga_per_hari)

                except ValueError:
                    print("\n========================")
                    print("Masukan harus berupa angka")
                    print("========================")

            elif sub_input_satu == "3":
                try:
                    merk = input("Masukan merk kendaraan : ")
                    harga_per_hari = int(input("Masukan biaya sewa per hari : "))
                    tambah_kendaraan("truk", merk, harga_per_hari)

                except ValueError:
                    print("\n========================")
                    print("Masukan harus berupa angka")
                    print("========================")

            else:
                print("\n=============================")
                print("Tipe kendaraan tidak tersedia")
                print("=============================")

        elif input_menu == "2":
            tampilkan_kendaraan()

        elif input_menu == "3":

            try:
                tampilkan_kendaraan()
                input_kendaraan = int(input("Pilih kendaraan: ")) - 1
                hari = int(input("Masukan jumlah hari: "))

                print(
                    f"Total biaya sewa untuk {hari} hari adalah Rp {list_kendaraan[input_kendaraan].biaya_sewa(hari)}"
                )
            except ValueError:
                print("\n==========================")
                print("Masukan harus berupa angka")
                print("==========================")

            except IndexError:
                print("\n===============================")
                print("Index kendaraan tidak ditemukan")
                print("===============================")

        elif input_menu == "4":
            break

        else:
            print("\n===================")
            print("Menu tidak tersedia")
            print("===================")

    print("\nTerimakasih telah menggunakan program ini")


if __name__ == "__main__":
    main()
