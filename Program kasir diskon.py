def hitung_total_belanja(total_belanja):
    if total_belanja >= 500_000:
        diskon = 0.20
    elif total_belanja >= 250_000:
        diskon = 0.10
    else:
        diskon = 0.0

    jumlah_diskon = total_belanja * diskon
    total_bayar = total_belanja - jumlah_diskon

    return jumlah_diskon, total_bayar

# Input dari pengguna
try:
    total = float(input("Masukkan total belanja (Rp): "))
    diskon, bayar = hitung_total_belanja(total)

    print(f"Diskon: Rp{diskon:,.0f}")
    print(f"Total yang harus dibayar: Rp{bayar:,.0f}")

except ValueError:
    print("Input harus berupa angka.")