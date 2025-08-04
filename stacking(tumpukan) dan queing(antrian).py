print("+"*25,"Stacking","+"*25)

stacking =[1,2,3,4,5]
print('data sekarang : ',stacking)
print("+"*50)

#Memasukan Data baru dengan append
stacking.append(6)
print('data masuk : ',6)
print('data sekarang',stacking)

stacking.append(7)
print('data masuk : ',7)
print('data sekarang',stacking)
print("+"*50)

print("+"*10,"Stacking Area","+"*10)
stacking.pop()
print("+"*35)
print('data sekarang',stacking)

stacking.pop()
print("+"*35)
print('data sekarang',stacking)

stacking.pop()
print("+"*35)
print('data sekarang',stacking)

stacking.pop()
print("+"*35)
print('data sekarang',stacking)

stacking.pop()
print("+"*35)
print('data sekarang',stacking)


stacking.pop()
print("+"*35)
print('data sekarang',stacking)

print("+"*25,"queing","+"*25)

from collections import deque
queing=deque([1,2,3,4,5])
print("Data Sekarang : ",queing)

print("+"*50)
#Data ditambahkan dengan append
queing.append(6)
print("Data Yang Di tambahkan : ",6)
print("Data Sekarang : ",queing)

print("+"*50)
#Data ditambahkan dengan append
queing.append(7)
print("Data Yang Di tambahkan : ",7)
print("Data Sekarang : ",queing)
print("+"*50)

#Mengurangi antrian
out=queing.popleft()
print("Data Yang Di Kurangi : ",out)
print("Data Sekarang : ",queing)
print("+"*50)

out=queing.popleft()
print("Data Yang Di Kurangi : ",out)
print("Data Sekarang : ",queing)
print("+"*50)

out=queing.popleft()
print("Data Yang Di Kurangi : ",out)
print("Data Sekarang : ",queing)
print("+"*50)

out=queing.popleft()
print("Data Yang Di Kurangi : ",out)
print("Data Sekarang : ",queing)
print("+"*50)