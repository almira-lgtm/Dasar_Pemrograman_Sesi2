jam_kerja = int(input("Masukkan Jam Kerja Kamu : "))
menit = int(input("Masukkan Jam Kerja Kamu : "))
gaji_perjam = float(input("Masukkan Gaji Per Jam : "))
total_jam_kerja = jam_kerja + (menit / 60)
total_gaji = total_jam_kerja * gaji_perjam
print("Total Jam Kerja : ",total_jam_kerja)
print("Total Gaji : ",total_gaji)