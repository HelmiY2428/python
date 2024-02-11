# Helmi Yahya 18.14.1.0035 Kelompok 1
#kondisi if
nilai = 9
if(nilai > 5):
    print("Selamat anda lulus ujian")
if(nilai > 7):
    print("selamat anda lulus")

#Kondisi IF-ELSE
nilai = 3
if (nilai > 7):
    print("selamat anda lulus")
else:
    print("maaf anda tidak lulus")

#Kondisi ELIF
hari_ini = "minggu"
if(hari_ini == "senin"):
    print("saya akan kuliah")
elif(hari_ini == "selasa"):
    print("saya akan kuliah")
elif(hari_ini == "rabu"):
    print("saya akan kuliah")
elif(hari_ini == "kamis"):
    print("saya akan kuliah")
elif(hari_ini == "jumat"):
    print("saya akan kuliah")
elif(hari_ini == "sabtu"):
    print("saya akan kuliah")
elif(hari_ini == "minggu"):
    print("saya akan libur")

#pengulangan while
angka = 8
if angka > 2:
    print ("if, nilai angka sekarang: " + str(angka))
    while angka > 2:
        print ("while, nilai angka sekarang: " + str(angka))
        angka = angka-1
