print("MJ Tea")
print()

print("""
        Daftar Menu Minuman :
        1. Es Teh Manis : Rp. 4.000
        2. Es Jeruk     : Rp. 5.000
        3. Es Lemon Tea : Rp. 7.000

""")

#Deklarasi Variabel
hargaTehManis=4000
hargaJeruk=5000
hargaLemonTea=7000

#Proses Input Data

a = input("Input Pesanan : ")

if(a=="1"):
    print("Anda Memesan Teh Manis dengan Harga",hargaTehManis)
else:
    print("Anda Belum Memesan Apa-apa")
