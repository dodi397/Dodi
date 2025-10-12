# Program Penentuan Jenis Segitiga berdasarkan Panjang Sisi

# Input panjang sisi
a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))

# Cek apakah bisa membentuk segitiga
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or a == c or b == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Bukan segitiga, karena tidak memenuhi syarat segitiga.")