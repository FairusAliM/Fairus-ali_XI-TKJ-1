# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def pangkat(bilangan, eksponen):
    return bilangan ** eksponen

# Contoh penggunaan
bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))
hasil_pangkat = pangkat(bilangan, eksponen)
print(f"Hasil dari {bilangan}^{eksponen} adalah: {hasil_pangkat}")
