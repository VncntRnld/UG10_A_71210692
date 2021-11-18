print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisal hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar rubik sebuah bilangan")

menu = int(input("Masukkan menu yang anda pilih: "))

#Proses
if menu==1:
    b11 = float(input("Masukkan bilangan yang ingin dibagi: "))
    b12 = float(input("Masukan bilangan pembagi: "))

    j1 = b11%b12

    print("Sisa hasil bagi {} dibagi dengan {} adalah {}" .format(b11, b12, j1))

elif menu==2:
    b21 = float(input("Masukkan bilangan yang ingin dibagi: "))
    b22 = float(input("Masukkan bilangan pembagi: "))

    j21 = b21/b22-0.5
    j22 = round(j21)

    print("Hasil pembagian {} dibagi dengan {} dibulatkan kebawah adalah {}" .format(b21, b22, j22))

elif menu==3:
    b31 = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    
    j31 = b31**1/3

    print("Akar kubik dari {} adalah {}" .format(b31, j31))

else:
    print("Menu yang anda pilih tidak tersedia")