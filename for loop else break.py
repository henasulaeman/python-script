number=12
for i in range(0,10):
    print(i)
    if i is number:
        print('data di temukan',i)
        break
else:
    print("data tidak di temukan")