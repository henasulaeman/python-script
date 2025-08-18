def cetak_umur(nama, bulan_lahir, tgl_lahir,tahun_lahir):
    from datetime import datetime
    tahun_ini = datetime.now().year
    cek_umur = tahun_ini - tahun_lahir
    print("Nama anda : ", nama)
    print("Tanggal Lahir Anda : ", tgl_lahir)
    print("Bulan Lahir anda : ", bulan_lahir)
    print("Umur anda adalah ",cek_umur)

nama = input("Nama Anda : ")
bulan_lahir = str(input("Bulan Lahir : "))
tgl_lahir = int(input ("Tanggal Lahir : "))
tahun_lahir = int(input ("Tahun Lahir : "))

cetak_umur (nama, bulan_lahir, tgl_lahir, tahun_lahir)