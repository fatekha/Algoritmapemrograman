#input identitas 
NIM = int(input("Masukkan NIM anda: "))
Nama = str(input("Masukkan Nama anda: "))
Kelas = str(input("Masukkan Kelas anda: "))
Prodi = str(input("Masukkan Prodi anda: "))
#input jari-jari dan phi
jari = float(input("Berapa jari-jari lingkaran: "))
phi = float(input("Masukkan nilai phi: "))
#rumus lingkaran
luas = phi * jari * jari
keliling = 2*phi*jari

print("----------------------------------------")
print("      OPERASI ARITMATIKA      ")
print("----------------------------------------")
print("NIM: %d" % (NIM))
print("Nama: %s" % (Nama))
print("Kelas: %s" % (Kelas))
print("Prodi: %s" % (Prodi))
print("----------------------------------------")
print("          LINGKARAN           ")
print("----------------------------------------")
print("Jari-jari lingkaran: %d" % (jari))
print("Nilai phi: %d" % (phi))
print("Luas lingkaran: %d" % (luas))
print("keliling lingkaran: %d" % (keliling))

list =["Uniss", "di", "belajar", "pada", "Mahasiswa", "pemrograman", "ruang", "lab", "algoritma", "semester", "topik", "data","tipe", "dan", "dengan", "Batang", 2]
#foword
print("----------------------------------------------------")
print("         Urutan Kata Yang Benar         ")
print("----------------------------------------------------")
print(list[4]) 
print(list[9]) 
print(list[16]) 
print(list[2])
print(list[8])
print(list[5])
print(list[14])
print(list[10])
print(list[12])
print(list[11])
print(list[1]) 
print(list[6])
print(list[7])
print(list[1])
print(list[0])
print(list[15])
print("----------------------------------------------------")
print("      menjadi rangkaian kalimat      ")
print("----------------------------------------------------")
#spok 
print("Mahasiswa semester 2 belajar algoritma pemrograman dengan topik tipe data di ruang lab di Uniss Batang.")
