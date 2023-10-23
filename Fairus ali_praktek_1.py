# Membaca total belanjaan pelanggan dari input pengguna
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Menghitung diskon berdasarkan aturan
if total_belanjaan > 500000:
    diskon = 0.10  # Diskon 10% untuk total belanjaan > 500.000
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05  # Diskon 5% untuk total belanjaan antara 300.000 dan 500.000
else:
    diskon = 0  # Tidak ada diskon untuk total belanjaan kurang dari 300.000

# Menghitung jumlah diskon
jumlah_diskon = total_belanjaan * diskon

# Menghitung total yang harus dibayar setelah diskon
total_setelah_diskon = total_belanjaan - jumlah_diskon

# Menampilkan hasil
print(f"Total belanjaan: Rp {total_belanjaan:.2f}")
print(f"Diskon: Rp {jumlah_diskon:.2f}")
print(f"Total setelah diskon: Rp {total_setelah_diskon:.2f}")