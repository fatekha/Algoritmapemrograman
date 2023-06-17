a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

#menghitung (a+b) (bxc)/(a+b+c)
result_a = (a+b)*(b*c)/(a+b+c)
print("Hasil dari (a+b) (bxc)/(a+b+c) adalah:",result_a )

# Menghitung P x L x t
result_b = a * b * c
print("Hasil dari P x L x t adalah:", result_b)

# Menghitung 1/2 x a x t
result_c = 0.5 * a * c
print("Hasil dari 1/2 x a x t adalah:", result_c)

# Menghitung (a + b)² + (b + c)² / ab
result_d = ((a + b) ** 2 + (b + c) ** 2) / (a * b)
print("Hasil dari (a + b)² + (b + c)² / ab adalah:", result_d)
