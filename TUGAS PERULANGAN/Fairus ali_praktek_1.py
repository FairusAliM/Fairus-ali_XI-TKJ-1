# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

jumlah_ayam = 100
target_ayam = 200
bulan = 0

while jumlah_ayam <= target_ayam:
    bulan += 1
    jumlah_ayam += jumlah_ayam * 0.05  # Menambahkan 5% dari jumlah ayam sebelumnya
    print(f"Bulan {bulan}: Jumlah ayam = {jumlah_ayam:.2f} ekor")

print(f"Dibutuhkan {bulan} bulan agar jumlah ayam melebihi {target_ayam} ekor.")
