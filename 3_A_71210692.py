pola = str(input("Mendatar/Menurun? : "))

if pola=="Mendatar" or pola=="mendatar":
    kelipatan = int(input("Masukkan Kolom: "))

    print("#"*kelipatan)

elif pola=="Menurun" or pola=="menurun":
    kelipatan = int(input("Masukkan baris: "))

    for datar in range(kelipatan):
        print("*")

else:
    print("Pola tidak dikenali")