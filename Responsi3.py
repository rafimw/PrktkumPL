jam_regular = int(input("Masukka jumlah jam kerja anda seminggu = "))
if jam_regular <= 48 :
    tot_gaji = jam_regular * 2000 
    print("Gaji anda adalah = ", tot_gaji)
elif jam_regular > 48 :
    jam_lembur = jam_regular - 48
    tot_gaji = jam_regular * 2000 
    gaji_lembur = jam_lembur*3000
    tot_gajilembur = tot_gaji + gaji_lembur
    print("Gaji lembur anda = ",gaji_lembur)
    print("Gaji regular = ", tot_gaji)
    print("Maka gaji total anda adalah = ",tot_gaji, "+", gaji_lembur)
    print("Maka gaji anda adalah = ", tot_gajilembur)