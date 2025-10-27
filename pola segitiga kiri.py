#Pola segitiga kiri
print("\n2. Pola segitiga tengah:")
for i in range(1, 6):
    # Cetak spasi di depan
    for j in range(5 - i):
        print(" ", end="")
    # Cetak bintang
    for j in range(2 * i - 1):
        print("*", end="")
    print()