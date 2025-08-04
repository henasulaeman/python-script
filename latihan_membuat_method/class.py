class Mahasiswa():
    nama="nama"
    def belajar(self,kondisi):
        print(self.nama,"Sedang belajar",kondisi)
        
    def tidur(self,kondisi):
        print(self.nama,"Sedang Tidur",kondisi)

juned=Mahasiswa()
jeni=Mahasiswa()

juned.nama="juned codet"
jeni.nama="jeni berani"

#print(juned.nama)
#print(jeni.nama)
juned.belajar("dengan giat")
jeni.tidur("Pulas")