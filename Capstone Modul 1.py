# Inisialisasi dictionary untuk daftar produk
daftar_produk_dict = {}

# Data awal untuk daftar produk, stok, harga, dan merek
sku = [101, 102, 103]
daftar_produk = ['Laptop', 'HP', 'TV']
stock = [10, 20, 15]
harga = [10000000, 8000000, 15000000]
merek = ['Acer', 'Mi', 'Apple']

# Membuat dictionary daftar_produk_dict dari data awal
for i in range(len(sku)):
    daftar_produk_dict[sku[i]] = {
        'nama': daftar_produk[i],
        'stock': stock[i],
        'harga': harga[i],
        'merek': merek[i] 
    }

# Fungsi untuk menampilkan daftar produk
def tampilkan_daftar_produk():
    print("Daftar Produk:")
    print("SKU\t|Nama\t\t|Merek\t\t|Stock\t|Harga")
    for key, value in daftar_produk_dict.items():
        formatted_harga = "{:,}".format(value['harga'])  # Format harga dengan koma
        print(f"{key}\t|{value['nama']}\t\t|{value['merek']}\t\t|{value['stock']}\t|{formatted_harga}")

# Fungsi untuk menambahkan produk baru
def tambah_produk():
    produk_baru = input("Masukkan nama produk baru: ")
    merek_baru = input("Masukkan merek produk baru: ")
    stock_baru = int(input("Masukkan jumlah stok produk baru: "))
    harga_baru = int(input("Masukkan harga produk baru (tanpa koma): "))

    max_sku = max(daftar_produk_dict.keys())
    new_sku = max_sku + 1

    daftar_produk_dict[new_sku] = {
        'nama': produk_baru,
        'merek': merek_baru,
        'stock': stock_baru,
        'harga': harga_baru
    }

    print("Daftar Produk:")
    tampilkan_daftar_produk()
    print(f"{produk_baru} ({merek_baru}) berhasil ditambahkan ke daftar produk.")

# Fungsi untuk menghapus produk
def hapus_produk():
    print("Daftar Produk:")
    tampilkan_daftar_produk()

    produk_hapus = int(input("Masukkan nomor SKU produk yang ingin dihapus: "))
    if produk_hapus in daftar_produk_dict:
        del daftar_produk_dict[produk_hapus]
        print("Daftar Produk setelah menghapus:")
        tampilkan_daftar_produk()
        print("Produk berhasil dihapus dari daftar.")
    else:
        print("Nomor SKU produk tidak valid.")

# Fungsi untuk melakukan pembelian produk
def beli_produk():
    print("Daftar Produk:")
    tampilkan_daftar_produk()

    total_harga = 0
    beli_lagi = True

    while beli_lagi:
        produk_beli = int(input("Masukkan nomor SKU produk yang ingin dibeli: "))
        if produk_beli in daftar_produk_dict:
            if daftar_produk_dict[produk_beli]['stock'] > 0:
                print(f"Stok {daftar_produk_dict[produk_beli]['nama']} tinggal {daftar_produk_dict[produk_beli]['stock']} unit.")
                qty_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
                if qty_beli <= daftar_produk_dict[produk_beli]['stock']:
                    total_harga += qty_beli * daftar_produk_dict[produk_beli]['harga']
                    print("Nama\t\t|Qty\t|Harga")
                    print(f"{daftar_produk_dict[produk_beli]['nama']}\t\t|{qty_beli}\t|{daftar_produk_dict[produk_beli]['harga']}")

                    daftar_produk_dict[produk_beli]['stock'] -= qty_beli

                    beli_lain = input("Mau beli yang lain? (Ya/Tidak): ").lower()
                    if beli_lain != "ya":
                        beli_lagi = False
                else:
                    print(f"Stok tidak cukup, Stok {daftar_produk_dict[produk_beli]['nama']} tinggal {daftar_produk_dict[produk_beli]['stock']} unit.")
            else:
                print("Maaf, stok produk habis.")
        else:
            print("Nomor SKU produk tidak valid.")

    print(f"Total yang harus dibayar = {total_harga}")
    while True:
        jumlah_uang = int(input("Masukkan jumlah uang = "))
        if jumlah_uang >= total_harga:
            uang_kembali = jumlah_uang - total_harga
            print(f"Terimakasih Telah Berbelanja Uang kembali anda = {uang_kembali}")
            break
        else:
            kurang_uang = total_harga - jumlah_uang
            print(f'Uang Anda Kurang {kurang_uang}, silahkan masukkan jumlah yang cukup')

# Fungsi utama
def main():
    while True:
        print('''
              Selamat Datang di Toko Elektronik

              List Menu:
              1. Menampilkan daftar produk
              2. Menambah produk
              3. Menghapus produk
              4. Membeli produk
              5. Exit program
              ''')
        menu = int(input('Masukkan menu yang ingin dijalankan: '))

        if menu == 1:
            tampilkan_daftar_produk()

        elif menu == 2:
            tambah_produk()

        elif menu == 3:
            hapus_produk()

        elif menu == 4:
            beli_produk()

        elif menu == 5:
            print("Terima kasih telah berbelanja di Toko Elektronik. Sampai jumpa!")
            break

        else:
            print("Menu tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
