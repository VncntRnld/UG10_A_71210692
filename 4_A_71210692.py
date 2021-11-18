artikel = str(input("Masukkan artikel yang ingin dipindai: "))

#input untuk artikel hanya bekerja jika diketik secara manual
#akan kacau jika di copas langsung dari pdf nya :v

cari1 = str(input("Masukkan nama klub favorit anda: "))
cari2 = str(input("Masukkan skor yang ingin dicari: "))

#gajadi dipakek
#hasil1 = artikel.index(cari1)
#hasil2 = artikel.index(cari2)

if (cari1 in artikel) and (cari2 in artikel):
    print("Hasil pencarian ditemukan")

elif (cari1 in artikel) and not(cari2 in artikel):
    print("Hanya {} yang ditemukan pada artikel ini" .format(cari1))

elif not(cari1 in artikel) and (cari2 in artikel):
    print("Hanya {} yang ditemukan pada artikel ini" .format(cari2))

else:
    print("Hasil pencarian {} dan {} tidak ditemukan" .format(cari1, cari2))