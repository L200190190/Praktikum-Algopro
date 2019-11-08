Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Ramadhana Wahid Aji Pamungkas'
>>> NIM = 190
>>> Tinggi = 1.71
>>> Berat = 65
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # karena tuple ditulis dengan tanda kurung dan tiap elemen ditulis secara urut dipisahkan dengan tanda koma
>>> Aku[0]
2000
>>> # karena data pertama dalam "Aku" adalah TahunLahir
>>> a = NIM % 4;Aku[a]
1.71
>>> # karena "a" menghasilkan tipe float maka data yang berada di "Aku" menampilkan data "Tinggi"
>>> type(Aku[a])
<class 'float'>
>>> # karena hasil dari Aku[a] adalah data "Tinggi" yang berisi data float
>>> Aku[a:4]
(1.71, 190)
>>> # karena dalam "Aku" data ke 4 adalah "NIM" maka akan menampilkan data "NIM" dan data ke a berisi data "Tinggi"
>>> type(Aku[4])
<class 'str'>
>>> # karena data ke 4 dari "Aku" berisi Nama yang merupakan tipe string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # karena "Aku" adalah tuple dan tuple berbeda dengan list
>>> type(Data)
<class 'list'>
>>> # karena list ditulis dengan tanda kurung siku dan elemen pada list dapat diubah sedangkan elemen pada tuple tidak dapat diubah
>>> type(Data[4])
<class 'str'>
>>> # karena isi data dari variabel "Data" adalah "Nama" yang bertipe string
>>> Data[4][5]
'h'
>>> # karena data ke 4 dari variabel "Nama" jadi [5] memeriksa variabel "Nama" urutan no 5 adalah huruf h bertipe string
>>> Data[4][a:6]
'madh'
>>> # karena data ke 4 dari variabel "Data" adalah "Nama", dan [a:6] yaitu perintah mengambil objek dari urutan ke 2 sampai sebelum urutan ke 6
>>> Data[0] = 'ok';Data
['ok', 65, 1.71, 190, 'Ramadhana Wahid Aji Pamungkas']
>>> # karena terdapat perintah mengganti elemen yaitu Data[0] = 'ok' jadi data pertama yang tersimpan di "Data" akan berubah menjadi 'ok'
>>> Data[-a]
190
>>> # karena ada perintah -a jadi menghitung data dari sebelah kanan jadi mengambil data NIM
>>> range(a)
range(0, 2)
>>> # karena range a sebesar 0,2
