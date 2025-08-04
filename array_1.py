string1="GIT BASH"
string2="Ini adalah string"
data1=[2,9,4,3,5,1]
data2=[1,4,7,2,4,9]
#Akses List
subdata1=data1[1]
subdata2=data2[-4]
#Memotong List
subdata3=data1[0:4]
subdata4=data2[:-2]
#Menambah List
subdata5=[100,200,300,400,500]
hasil1=data1+subdata5
#Merubah data dari List
#hasil2=subdata5[0]=500
#print(subdata5)
a=subdata5[:] #[:] Fungsinya data subdata5 akan di coppykan ke a , kalu tidak menggunakan [:] maka menjadi sharing data
a[1]=70
#merubah data array dengan methode slicing
subdata5[3:5]=[11,12]
#array dalam array
x=[data1,data2]
#mengakses array dalam multidimensi array
y=x[1][2]
#print(x)
#print(y)
#method List menggunakan append
print(data1)
data1.append(50)
print(data1)
#Function yang bisa kita gunakan kepada list
panjang_list=len(data1)
print(panjang_list)


