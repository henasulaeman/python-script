Barang=['kompor','katel','piring','sendok','gelas']

#Menambah Data ke dalam array menggunakan append
Barang.append('garpu')
print(Barang)
print("+"*100)

#Menambah karakter ke dalam list array menggunakan extend
Barang.extend('panci')
print(Barang)
print("+"*100)

#Menghitung Jumlah data yang ada di dalam List menggunakan count
JumlahData=Barang.count('kompor')
print(JumlahData)
print("+"*100)

#Insert data yang ada di dalam List menggunakan insert
Barang.insert(3,'ember')
print(Barang)
print("+"*100)
#Remove data yang ada di dalam List menggunakan remove
Barang.remove('ember')
print(Barang)
print("+"*100)

#Coppy data yang ada di dalam List menggunakan copy
#Jika tidak mencantumkan .copy()
stuf=Barang
stuf.insert(3,'Mobil')
print(stuf)
print(Barang)
print("+"*100)
#Coppy data yang ada di dalam List menggunakan copy
#Jika mencantumkan .copy()
stuff=Barang.copy()
stuff.insert(3,'Motor')
print(stuff)
print(Barang)
print("+"*100)

