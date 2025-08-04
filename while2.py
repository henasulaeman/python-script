angka=0

while angka <10:
    if angka is 5:
        print("Check 1")
        angka +=1 #agar tidak membuat infinit loop
        break
    print("Ini dalam while")
    angka +=1
else:
    print("nilai di akhir while adalah",angka)