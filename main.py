import json
import os


def tambah_data():
    nama = input("Masukkan nama barang: ")
    print(f"Barang '{nama}' berhasil dicatat!")

def main():
    while True:
        print("\n1. Tambah Data")
        print("2. Keluar")

        pilihan = input("pilih menu: ")

        if pilihan == "1":
            tambah_data() #panggil fungsi tambah_data
        elif pilihan == "2":
            print("Sampai jumpa! ")
            break


if __name__ == "__main__":
    main()