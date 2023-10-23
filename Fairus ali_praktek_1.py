# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan.

total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

if total_belanjaan > 500000:
    diskon = 0.10 
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05 
else:
    diskon = 0  

jumlah_diskon = total_belanjaan * diskon

total_setelah_diskon = total_belanjaan - jumlah_diskon

print(f"Total belanjaan: Rp {total_belanjaan:.2f}")
print(f"Diskon: Rp {jumlah_diskon:.2f}")
print(f"Total setelah diskon: Rp {total_setelah_diskon:.2f}")