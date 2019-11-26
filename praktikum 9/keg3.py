import shelve

berkas = open("L200190190", "r")
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()
TTL = Kota + "," + TTL
berkas.close()

F = shelve.open("Ramadhana.data")
F["Data"] = (NIM, TTL, Nama, Kota)
F.close()
