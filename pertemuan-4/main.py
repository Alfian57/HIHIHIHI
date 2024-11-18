def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."
    else:
        return result


if __name__ == "__main__":
    num1 = 10
    num2 = 0
    print(divide_numbers(num1, num2))

    # num3 = "10"
    # num4 = 2
    # print(divide_numbers(num3, num4))


"""
- ValueError: Dilemparkan ketika fungsi menerima argumen dengan tipe yang benar tetapi nilai yang tidak sesuai.
- TypeError: Dilemparkan ketika operasi atau fungsi diterapkan pada objek dengan tipe yang tidak sesuai. Nilai yang terkait adalah string yang memberikan detail tentang ketidakcocokan tipe.
- IndexError: Dilemparkan ketika subskrip urutan berada di luar jangkauan.
- KeyError: Dilemparkan ketika kunci kamus tidak ditemukan.
- AttributeError: Dilemparkan ketika atribut yang diminta tidak ditemukan.
- ZeroDivisionError: Dilemparkan ketika argumen kedua dari operasi pembagian atau modulo adalah nol.
- RuntimeError: Dilemparkan ketika kesalahan yang dihasilkan tidak termasuk dalam kategori apa pun.
"""
