#PROGRAM PEMINJAMAN ASET DI DIREKTORAT MANAJEMEN ASET#

#Input Data Peminjman

# nama =input("Masukan Nama Peminjaman : ")
# keperluan = input("Masukan Keperluan Peminjaman : ")
# nama_aset= input("Masukan Aset Yang di Pinjam : ")
# durasi=input("Masukan Durasi Peminjaman : ")
# acc = input("Masukan Persetujuan Silahkan Isi Ya/Tidak : ")

# if acc == "Ya":
#     print("Atas Nama",nama," di ACC untuk Meminjam aset ",nama_aset)

# elif acc == "Tidak":
#     print("Atas Nama",nama,"TIDAK ACC untuk Meminjam aset ",nama_aset)



def peminjam_acc (nama,keperluan,nama_aset,durasi,acc):
    print ("Atas Nama",nama," di ACC untuk Meminjam aset ",nama_aset)

def peminjam_no_acc (nama,keperluan,nama_aset,durasi,acc):   
    print("Atas Nama",nama,"TIDAK ACC untuk Meminjam aset ",nama_aset)


nama =input("Masukan Nama Peminjaman : ")
keperluan = input("Masukan Keperluan Peminjaman : ")
nama_aset= input("Masukan Aset Yang di Pinjam : ")
durasi=input("Masukan Durasi Peminjaman : ")
acc = input("Masukan Persetujuan Silahkan Isi Ya/Tidak : ")


if acc == "Ya":
    peminjam_acc(nama,keperluan,nama_aset,durasi,acc)

elif acc == "Tidak":
    peminjam_no_acc(nama,keperluan,nama_aset,durasi,acc)