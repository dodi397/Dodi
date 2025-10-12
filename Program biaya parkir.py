# Program Biaya Parkir

# Input durasi parkir dalam jam
jam = float(input("Masukkan durasi parkir (dalam jam): "))

# Menentukan biaya parkir
if jam <= 2:
    biaya = 5000
elif 3 <= jam <= 5:
    biaya = 10000
elif jam > 5:
    biaya = 15000
else:
    biaya = 0  # Jika input tidak valid

# Output hasil
print(f"Biaya parkir untuk {jam} jam adalah Rp{biaya:,}")