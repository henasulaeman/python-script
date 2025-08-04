def guru(nama,pelajaran):
    print("Nama Guru Anda",nama)
    print("Mengajar",pelajaran)

def siswa(nama,kelas):
    print("nama siswa adalah",nama)
    print("Kelas ",kelas)

def penjagaSekolah(nama,shift="malam",galak="sangat"): #Menggunakan nilai default
    print("Nama penjaga sekolah",nama)
    print("kerjanya shiff apa",shift)
    print("Apakah penjaganya galak ?",galak)

guru("Hena Sulaiman","Pemograman komputer")
siswa("Sandi Mn","3 SMA")
penjagaSekolah("Mang ujang") #tidak diisi karena sudah ada nilai default