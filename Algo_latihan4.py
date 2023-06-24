print("--------------------------------------")
print(" Toko berkah mulia ")
print("--------------------------------------")

# setting variabel qty
beli1 = int(input("Berapa sarimi yang ingin dibeli? "))
beli2 = int(input("Berapa minuman segar yang ingin dibeli? "))
beli3 = int(input("Berapa gula pasir yang ingin dibeli? "))
beli4 = int(input("Berapa beras yang ingin dibeli? "))
beli5 = int(input("Berapa telur yang ingin dibeli? "))

# setting variabel harga satuan
sarimi = int(input("Harga satuan sarimi? "))
mingar = int(input("Harga satuan minuman segar? "))
gusir = int(input("Harga satuan gula pasir? "))
beras = int(input("Harga satuan beras? "))
telur = int(input("Harga satuan telur? "))

# seting variabel jumlah
jumlah1 = beli1 * sarimi
jumlah2 = beli2 * mingar
jumlah3 = beli3 * gusir
jumlah4 = beli4 * beras
jumlah5 = beli5 * telur

# nama produk | qty | harga satuan | jumlah
print("-------------------------------------------------------")
print("Nama Produk       | Qty   | Harga Satuan  | Jumlah ")
print("1. Sarimi          =", beli1, "    ", sarimi, "          ", jumlah1)
print("2. Minuman Segar   =", beli2, "    ", mingar, "          ", jumlah2)
print("3. Gula Pasir      =", beli3, "    ", gusir, "          ", jumlah3)
print("4. Beras           =", beli4, "    ", beras, "          ", jumlah4)
print("5. Telur           =", beli5, "    ", telur, "          ", jumlah5)
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
