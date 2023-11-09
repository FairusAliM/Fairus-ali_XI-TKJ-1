# nama = Fairus ali muzaki
# absen = 07
# kelas = XI-TKJ 1
# soal = Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def jumlah_digit(bilangan):
    return sum(int(digit) for digit in str(abs(bilangan)))

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan: "))
hasil_jumlah_digit = jumlah_digit(bilangan)
print(f"Jumlah digit dari {bilangan} adalah: {hasil_jumlah_digit}")
