#ini adalah program python pertama saya
nama=input("Masukan Nama Lengkap Anda :")
st_nkh=input("Status Menikah :")
gol=input("Golongan : ")
gaji_pokok=3500000


if st_nkh=="Menikah":

    tunjangan_keluarga=0.25*gaji_pokok
    totalUpah=gaji_pokok+int(tunjangan_keluarga)
    print("Total gajih bersih",gaji_pokok," + Tunjangan Keluarga ",tunjangan_keluarga,"=",totalUpah)
elif(gol=="A"):
    tunjangan_jabatan = 0.3 * gaji_pokok
    totalUpah = gaji_pokok + int(tunjangan_jabatan)
    print("Total gajih bersih", gaji_pokok, " + Tunjangan Keluarga ", tunjangan_jabatan, "=", totalUpah)
elif(gol=="B"):
    tunjangan_jabatan = 0.25 * gaji_pokok
    totalUpah = gaji_pokok + int(tunjangan_jabatan)
    print("Total gajih bersih", gaji_pokok, " + Tunjangan Keluarga ", tunjangan_jabatan, "=", totalUpah)
elif(gol=="C"):
    tunjangan_jabatan = 0.15 * gaji_pokok
    totalUpah = gaji_pokok + int(tunjangan_jabatan)
    print("Total gajih bersih", gaji_pokok, " + Tunjangan Keluarga ", tunjangan_jabatan, "=", totalUpah)
