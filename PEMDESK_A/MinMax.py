bil = []

n = int(input("Masukkan jumlah angka yang akan diinput : "))

for i in range(n):
    masuk = int(input("Masukkan angka : "))
    bil.append(masuk)

bil.sort()

print(bil)

max = bil[n - 1]
min = bil[0]

print("Nilai terbesar dari bilangan yang anda input adalah : " + str(max))
print("Nilai terkecil dari bilangan yang anda input adalah : " + str(min))