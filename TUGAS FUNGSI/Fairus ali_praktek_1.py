# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2 * batas, 2):
        total += i
    return total

# Contoh penggunaan fungsi
batas_pengguna = int(input("Masukkan batas deret bilangan ganjil: "))
hasil_total = total_deret_ganjil(batas_pengguna)
print(f"Total deret bilangan ganjil hingga batas {batas_pengguna} adalah: {hasil_total}")
