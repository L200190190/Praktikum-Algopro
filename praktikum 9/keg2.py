file = open("L200190190", "w")
berkas = open("L200190190", "w")
berkas.write("L200190190\n")
berkas.write("11/27/2000\n")
berkas.write("Ramadhana W A P\n")
berkas.write("Karanganyar")
berkas.close()



file = open("L200190190", "r+")
NIM = file.readline()
TTL = file.readline()
Nama = file.readline()
Kota = file.readline()
TTL = Kota + "," + TTL
print(Nama)
print(TTL)
print(NIM)
file.close()


