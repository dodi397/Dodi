# Program untuk mengecek bilangan positif, negatif, atau nol

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah bilangan bulat: "))

# Mengecek kondisi bilangan
if angka > 0:
    print("Bilangan positif")
elif angka < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")