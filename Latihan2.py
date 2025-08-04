nama=input("Nama Konsumen :")
jumlah_tabungan=float(input("Masukan Jumlah Tabungan yan anda miliki"))

if 1<=jumlah_tabungan<=1000000:
    bunga=9/100
    getBunga=jumlah_tabungan*bunga
    tabunganKenaBunga=jumlah_tabungan-getBunga
    print("Jumlah Bunga Yang Di Dapat adalah ",bunga,"*",jumlah_tabungan," = ",getBunga)
    print("Jumlah Tabungan Kena Bunga adalah",tabunganKenaBunga)
elif 1000000<=jumlah_tabungan<=10000000:
    bunga = 12 / 100
    getBunga = jumlah_tabungan * bunga
    tabunganKenaBunga = jumlah_tabungan - getBunga
    print("Jumlah Bunga Yang Di Dapat adalah ", bunga, "*", jumlah_tabungan, " = ", getBunga)
    print("Jumlah Tabungan Kena Bunga adalah", tabunganKenaBunga)
elif 10000000 <= jumlah_tabungan<=100000000:
    bunga = 15 / 100
    getBunga = jumlah_tabungan * bunga
    tabunganKenaBunga = jumlah_tabungan - getBunga
    print("Jumlah Bunga Yang Di Dapat adalah ", bunga, "*", jumlah_tabungan, " = ", getBunga)
    print("Jumlah Tabungan Kena Bunga adalah", tabunganKenaBunga)
