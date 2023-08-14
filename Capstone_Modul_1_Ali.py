# Inisialisasi dictionary untuk daftar produk
daftar_produk_dict = {}

# Data awal untuk daftar produk, stok, harga, dan merek
sku = [101, 102, 103]
daftar_produk = ['Laptop', 'HP', 'TV']
stock = [10, 20, 15]
harga = [10000000, 8000000, 15000000]
merek = ['Acer', 'Mi', 'Apple']

# Membuat dictionary daftar_produk_dict dari data awal
for i in range(len(sku)): #Fungsi Loop untuk menambahkan Dict daftar product
    daftar_produk_dict[sku[i]] = {
        'nama': daftar_produk[i],
        'stock': stock[i],
        'harga': harga[i],
        'merek': merek[i] 
    }

# Fungsi untuk menampilkan daftar produk dengan format harga yang menggunakan koma
def tampilkan_daftar_produk():
    print("Daftar Produk:")
    print("SKU\t|Nama\t\t|Merek\t\t|Stock\t|Harga")
    for key, value in daftar_produk_dict.items(): #Mengakses Dict daftar product
        formatted_harga = "{:,}".format(value['harga'])  # Format harga dengan koma
        formatted_stock = "{:,}".format(value['stock'])  # Format stok dengan koma
        print(f"{key}\t|{value['nama']}\t\t|{value['merek']}\t\t|{formatted_stock}\t|{formatted_harga}")

# Fungsi untuk menambahkan produk
def tambah_produk():
    produk_baru = input("Masukkan nama produk baru: ")
    merek_baru = input("Masukkan merek produk baru: ")
    stock_baru = int(input("Masukkan jumlah stok produk baru: "))
    harga_baru = int(input("Masukkan harga produk baru (tanpa koma): ").replace(",", ""))  # Menghapus koma dari input harga

    max_sku = max(daftar_produk_dict.keys()) #Mengakses kata kunci
    new_sku = max_sku + 1 #Menambahkan keys yang baru

    daftar_produk_dict[new_sku] = {
        'nama': produk_baru,
        'merek': merek_baru,
        'stock': stock_baru,
        'harga': harga_baru
    }

    tampilkan_daftar_produk()
    print(f"{produk_baru} ({merek_baru}) berhasil ditambahkan ke daftar produk.")

# Fungsi untuk menghapus produk
def hapus_produk():
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

    formatted_total_harga = "{:,}".format(total_harga)  # Format total harga dengan koma
    print(f"Total yang harus dibayar = {formatted_total_harga}")
    while True:
        jumlah_uang = int(input("Masukkan jumlah uang = "))
        if jumlah_uang >= total_harga:
            uang_kembali = jumlah_uang - total_harga
            formatted_uang_kembali = "{:,}".format(uang_kembali)  # Format uang kembali dengan koma
            print(f"Terimakasih Telah Berbelanja Uang kembali anda = {formatted_uang_kembali}")
            break
        else:
            kurang_uang = total_harga - jumlah_uang
            formatted_kurang_uang = "{:,}".format(kurang_uang)  # Format jumlah uang yang kurang dengan koma
            print(f'Uang Anda Kurang {formatted_kurang_uang}, silahkan masukkan jumlah yang cukup')

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
