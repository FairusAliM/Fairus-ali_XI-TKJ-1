# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

nilai_investasi = 10000  # Nilai investasi awal dalam dollar
target_nilai = 20000  # Nilai investasi target dalam dollar
tahun = 0  # Jumlah tahun

while nilai_investasi <= target_nilai:
    tahun += 1
    nilai_investasi += nilai_investasi * 0.06  # Menambahkan 6% dari nilai investasi sebelumnya
    print(f"Tahun {tahun}: Nilai investasi = ${nilai_investasi:.2f}")

print(f"Dibutuhkan {tahun} tahun agar nilai investasi melebihi ${target_nilai:.2f}.")
