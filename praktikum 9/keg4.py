import shelve

berkas = open("L200190190", "r")
F = shelve.open("Ramadhana.data")
print(F["Data"][2])
print(F["Data"][0])
print(F["Data"][1])
F.close()
