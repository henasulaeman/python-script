# Hari 1 – Dasar Python & Variabel
#Buat program yang mencetak:
#Nama lengkapmu
#Umurmu
#Kota tempat tinggal
from datetime import datetime

nama = input("Tuliskan Nama Lengkap Anda : ")
bulan_lahir = input("Bulan Lahir : ")
tgl_lahir = input("Tanggal Lahir :")
tahun_lahir = input("Tahun Lahir :")
tahun_ini = datetime.now().year

cek_umur = int(tahun_ini) - int(tahun_lahir)

print ("Nama:",nama)
print ("Tanggal Lahir Anda :",tgl_lahir,"",bulan_lahir,"",tahun_lahir)
print("Anda Sekarang berumur : ",cek_umur)



#Buat program yang menghitung:
#Luas persegi panjang (input panjang & lebar)
#Keliling lingkaran (input jari-jari)