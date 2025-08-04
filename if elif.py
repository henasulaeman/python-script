nilai1=50
nilai2=60

#NESTING IF
if nilai1==80:
    print("Nilai Anda Adalah",nilai1)
    if nilai2==60:
        print("Nilai Anda Adalah",nilai2)

nilai3=100

if nilai3 is 100:
    print("Nilai Anda Adalah",nilai3)

if nilai3 is not 50:
    print("Nilai Anda Bukan 50")



print(50*"=")
nilai4=40

if 80 <= nilai4 <= 100:
    print("A")
elif 70 <= nilai4 < 80:
    print("B")
elif 60 <= nilai4 < 70:
    print("C")
elif 50 <= nilai4 < 60:
    print("D")
else:
    print("Maaf Anda Belum lulus matakuliah ini")

print(100*"+")

gorengan=["bakwan","cireng","bala-bala","gehu","pisang goreng","pukis"]
beli="cireng"

if beli in gorengan:
    print("ya saya jualan",beli)
elif not beli in gorengan:
    print("maaf saya tidak jual",beli)

#Atau Bisa juga seperti ini, bisa mencari karakter yang di simpan dalam 1 variabel
print(100*"+")
karakter="c"
if karakter in beli:
    print("Found, char adalah",karakter)
else:
    print("Not Found Karakter",karakter)