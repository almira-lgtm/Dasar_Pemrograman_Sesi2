jarak_tempuh = float(input("Masukkan jarak perjalanan yang ditempuh (km) : "))
km_per_liter = 40
harga_bensin = 13000
jumlah_liter_dibutuhkan = jarak_tempuh / km_per_liter
total_biaya = jumlah_liter_dibutuhkan * harga_bensin
print("Total Liter bensin yang dibutuhkan :", jumlah_liter_dibutuhkan)
print("Total biaya bensin :", total_biaya)