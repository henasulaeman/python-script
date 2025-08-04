class Mahasiswa():

    def __init__(self,input_nama,input_nim):
        self.nama=input_nama
        self.nim=input_nim
    def belajar(self,kondisi):
        print(self.nama,"Sedang Belajar",kondisi)
    def tidur(self,kondisi):
        print(self.nama,"Sedang Tidur",kondisi)

otong=Mahasiswa("otong surotong",12111077)
ujang=Mahasiswa("Sakurjang",12111077)

print(otong.nama,otong.nim)

#EASY ????? YES
