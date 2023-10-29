# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1

from datetime import datetime

# Input estimasi waktu selesai proyek dan tanggal target selesai
estimasi_selesai = input("Masukkan estimasi waktu selesai proyek (YYYY-MM-DD): ")
tanggal_target_selesai = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")

estimasi_selesai = datetime.strptime(estimasi_selesai, '%Y-%m-%d')
tanggal_target_selesai = datetime.strptime(tanggal_target_selesai, '%Y-%m-%d')

# Bandingkan tanggal dan cetak hasilnya
if estimasi_selesai <= tanggal_target_selesai:
    print("Tepat waktu")
else:
    print("Terlambat")