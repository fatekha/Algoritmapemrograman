# Open File 
data = open("data_iris.txt", "r")
print ("Nama File",data.name)

#read
file_konten = data.read(100)
print ("Isa Data:",file_konten[18:40])

#Closed
data.close()
# For Loops
#for i in range(1,10):
        #print(1)
list_dosen =("Mawar","selasa","Dedi","Lukman")
list_jatwal =("senin","selasa","rabu","kamis","jumat")

for i in (list_dosen):
  for k in (list_jatwal):
    print(i, " -" ,k)
    
    
# Fibonanci
n=10
fib = [0,1]

for i in range(n-2):
  fib_lanjut = fib[i+1] + fib[i]
  print(fib[i+1]," + ",fib[i]," = ",fib_lanjut)
  fib.append(fib_lanjut)
  print(fib)
