# Program konversi nilai angka ke nilai huruf

# Meminta input dari pengguna
nilai = int(input("Masukkan nilai angka (0-100): "))

# Mengecek rentang nilai
if 85 <= nilai <= 100:
    print("Nilai huruf: A")
elif 70 <= nilai <= 84:
    print("Nilai huruf: B")
elif 55 <= nilai <= 69:
    print("Nilai huruf: C")
elif 40 <= nilai <= 54:
    print("Nilai huruf: D")
elif 0 <= nilai < 40:
    print("Nilai huruf: E")
else:
    print("Input tidak valid, masukkan angka antara 0-100")