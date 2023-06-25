print("--------------------------------------")
print(" Toko berkah mulia ")
print("--------------------------------------")

# setting variabel qty
beli1 = int(input("Berapa sarimi yang ingin dibeli? "))
beli2 = int(input("Berapa minuman segar yang ingin dibeli? "))
beli3 = int(input("Berapa gula pasir yang ingin dibeli? "))
beli4 = int(input("Berapa beras yang ingin dibeli? "))
beli5 = int(input("Berapa telur yang ingin dibeli? "))

# setting harga satuan
harga1 = 5000
harga2 = 10000
harga3 = 25000
harga4 = 12000
harga5 = 30000

# setting variabel jumlah
jumlah1 = beli1 * harga1
jumlah2 = beli2 * harga2
jumlah3 = beli3 * harga3
jumlah4 = beli4 * harga4
jumlah5 = beli5 * harga5


# nama produk | qty | harga satuan | jumlah
print("-------------------------------------------------------")
print("Nama Produk       | Qty   | Harga Satuan   | Jumlah ")
print("1. Sarimi          =", beli1, "    ", harga1, "           ", jumlah1)
print("2. Minuman Segar   =", beli2, "    ", harga2, "          ", jumlah2)
print("3. Gula Pasir      =", beli3, "    ", harga3, "          ", jumlah3)
print("4. Beras           =", beli4, "    ", harga4, "          ", jumlah4)
print("5. Telur           =", beli5, "    ", harga5, "          ", jumlah5)
print("-------------------------------------------------------")

print("Diskon belanja >200 ribu sebesar 10%")
print("-------------------------------------------------------")

# total harga
total_harga = jumlah1 + jumlah2 + jumlah3 + jumlah4 + jumlah5

# Menghitung diskon jika total belanja > 200 ribu
diskon = 0
if total_harga > 200000:
    diskon = 0.1 * total_harga

# Menghitung total bayar setelah diskon
total_bayar = total_harga - diskon

print("Total Bayar: ", total_bayar)
