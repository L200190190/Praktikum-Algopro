## Program Akun
## Dibuat oleh Ramadhana L200190190
import random
angka = random.randint(0,1000)

Nama = 'Ramadhana Wahid Aji Pamungkas'
TanggalLahir = '27 November 2000'
NamaSingkat = Nama[0] + '. ' + Nama[10] + '. ' + Nama[16] + '. ' + Nama[20:29]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[12:16]
Password = Nama[0:3] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
