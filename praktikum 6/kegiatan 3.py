Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Ramadhana Wahid Aji Pamungkas'
>>> NIM = 'L200190190'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # karena data "x" berubah menjadi integer dengan perintah int
>>> type(b)
<class 'int'>
>>> # karena terdapat perintah "len" yang berfungsi mengembalikan panjang(jumlah anggota) dari suatu objek
>>> a / b
41.03448275862069
>>> # karena hasil dari 1190 dibagi 29 menghasilkan 41.03448275862069
>>> a // b
41
>>> # karena arti dari perintah "//" pembulatan ke bawah
>>> 10 * (a - 999)
1910
>>> # karena nilai dari a - 999 adalah 191, setelah itu dikali 10 menghasilkan nilai 1910
>>> b ** 2
841
>>> # karena arti dari perintah "**" adalah perpangkatan, dengan nilai b = 29
>>> a % b
1
>>> # karena arti dari perintah "%" adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # karena "12.5" adalah bilangan desimal
>>> a / c
95.2
>>> # karena nilai a = 1190 dan dibagi nilai c = 12.5
>>> a // c
95.0
>>> # karena arti dari perintah "//" pembulatan ke bawah
>>> a % c
2.5
>>> # karena arti dari perintah "%" adalah sisa hasil bagi
>>> c > b
False
>>> # karena nilai "c" tidak lebih besar dari nilai "b" jadi menghasilkan nilai false
>>> type(c > b)
<class 'bool'>
>>> # karena (c > b) merupakan jenis tipe data bool yang menghasilkan true atau false
>>> a > b and b > c
True
>>> # karena pernyataan a > b menghasilkan true dan pernyataan b > c menghasilkan true
>>> a > 1100 or b < 10
True
>>> # karena nilai a = 1190 dan ada perintah "or", walaupun pernyataan b < 10 menghasilkan false

