# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = : Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

jumlah_apel = 100  # Jumlah apel awal
sisa_apel = jumlah_apel
sisa_terkecil = 20  # Jumlah apel yang diinginkan

hari = 0  # Jumlah hari

while sisa_apel >= sisa_terkecil:
    hari += 1
    sisa_apel -= sisa_apel * 0.10  # Mengurangi 10% dari sisa apel sebelumnya
    print(f"Hari {hari}: Sisa apel = {sisa_apel:.0f} buah")

print(f"Dibutuhkan {hari} hari agar sisa apel kurang dari {sisa_terkecil} buah.")
