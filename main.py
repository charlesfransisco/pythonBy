import json
import os

# membaca apakah expenses.json sudah ada, mengubah isi json menjadi python list/
def load_data():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return []
expenses = load_data()

def tambah_data():
    try:
        amount = float(input("Masukkan jumlah pengeluaran: "))
    except ValueError:
        print("Nominal harus berupa angka. Silakan coba lagi.")
        return
    description = input("Masukkan deskripsi pengeluaran: ")

    expense = {
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Data pengeluaran berhasil ditambahkan!")

def tampilkan_data():
    if not expenses:
        print("Belum ada data pengeluaran.")
    else:
        print('\n=== Data Pengeluaran ====')

        for nomor, expense in enumerate(expenses, start=1):
            print(f"{nomor}."
                  f" {expense['description']}"
                  f" - Rp {expense['amount']}")
def simpan_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    print( "Data berhasil disimpan.")

def main():
    while True:
        print("\n1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Simpan Data")
        print("4. Keluar")

        pilihan = input("pilih menu: ")

        if pilihan == "1":
            tambah_data() #panggil fungsi tambah_data
        elif pilihan == "2":
            tampilkan_data() #panggil fungsi tampilkan_data
        elif pilihan == "3":
            simpan_data() #panggil fungsi simpan_data
        elif pilihan == "4":
            print("Sampai jumpa! ")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()