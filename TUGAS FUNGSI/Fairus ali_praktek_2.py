# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
hasil_faktorial = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah: {hasil_faktorial}")