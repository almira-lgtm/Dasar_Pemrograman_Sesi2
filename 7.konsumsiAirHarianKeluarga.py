jumlah_orang = int(input("Masukkan jumlah orang : "))
air_perorang = 2.5
jumlah_hari = 7
liter_per_galon = 19
harga_galon = 19000
total_air_perminggu = jumlah_orang * air_perorang * jumlah_hari
total_galon_yang_harus_dibeli = total_air_perminggu / liter_per_galon
biaya_yang_harus_dikeluarkan = total_galon_yang_harus_dibeli * harga_galon
print("Total Kebutuhan Air Perminggu : ",total_air_perminggu)
print("Jumlah Galon yang Harus Dibeli : ",total_galon_yang_harus_dibeli)
print("Total Biaya yang Harus Dikeluarkan  : ",biaya_yang_harus_dikeluarkan)
