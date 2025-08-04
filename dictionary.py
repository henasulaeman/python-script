#Dictionary
#variabel={keys:value,}
member1={"ID":101,
         "Nama":"Ujang Codet",
         "Pekerjaan":"Preman Pasar",
         "Status member":"Gold Sangar"}

member2={"ID":102,
         "Nama":"Ujang Pintu",
         "Pekerjaan":"Mebel Pintu",
         "Status Member":"Perak"}

memberList={101:member1,102:member2}

#print(member1["pekerjaan"])
#print(member1.keys())
#print(member1.values())
#print(member1.items())

print(memberList[101])