sodaraku=['rani','ratih','ria','rudi','sandi']
pekerjaan=['kasir','teller','marketing','kasir','programmer']

i=0;
for a in sorted(sodaraku):
    print(i,"Nama Sodaraku adalah",a)
    i+=1

print("+"*100)

#Menggunakan enumerate
for index,nama_sodara in enumerate(sodaraku):
    print(index,":",nama_sodara)

print("+"*100)

#Menggunakan zip : untuk menggabungkan List
for nm_sodara,pekerjaanya in zip(sodaraku,pekerjaan):
    print("Nama :",nm_sodara," Pekerjaannya adalah :", pekerjaanya)

print("+"*100)

#Menggunakan Dictionary
nama_band={"Peterpan":"Tak ada yang abadi",
           "Ada Band":"Surga Cinta",
           "Kuburan":"doremi",
           "syahrini":"jodohku"}
for i in nama_band.items():
    print(i)
