gaji_pokok = float(input("Masukkan total gaji pokok : "))
tunjangan = float(input("Masukkan total tunjangan : "))
gaji_kotor = gaji_pokok + tunjangan
bpjs = gaji_kotor * 0.02
pajak = gaji_kotor * 0.05
potongan = bpjs + pajak
gaji_bersih = gaji_kotor - potongan
print("Total Gaji bersih :", gaji_bersih)