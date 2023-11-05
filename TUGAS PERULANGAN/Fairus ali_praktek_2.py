# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal =Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarak = 5  # Jarak awal dalam kilometer
target_jarak = 10  # Jarak target dalam kilometer
minggu = 0  # Jumlah minggu

while jarak <= target_jarak:
    minggu += 1
    jarak += jarak * 0.10  # Menambahkan 10% dari jarak sebelumnya
    print(f"Minggu {minggu}: Jarak = {jarak:.2f} kilometer")

print(f"Dibutuhkan {minggu} minggu agar pelari dapat berlari lebih dari {target_jarak} kilometer.")
