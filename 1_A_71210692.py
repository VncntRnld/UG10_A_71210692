Rug = float(input("Masukkan nilai rata-rata UG anda:" ))
tts = float(input("Masukkan nilai TTS anda: "))
tas = float(input("Masukkan nilai TAS anda: "))
print("=============================")

#proses (na = nilai akhir)
NRug = Rug*70/100
Ntts = tts*15/100
Ntas = tas*15/100
na = NRug + Ntts + Ntas

print ("Nilai anda: {}" .format(na))

#penilaian huruf
if na<45:
    nh = "E"
elif na<55:
    nh = "D"
elif na<60:
    nh = "C"
elif na<65:
    nh = "C+"
elif na<70:
    nh = "B-"
elif na<75:
    nh = "B"
elif na<80:
    nh = "B+"
elif na<85:
    nh = "A-"
else:
    nh = "A"



print("Nilai huruf anda: {}" .format(nh))