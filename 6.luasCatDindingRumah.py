panjang = float(input("Masukkan panjang kamar : "))
lebar = float(input("Masukkan lebar kamar : "))
tinggi = float(input("Masukkan tinggi kamar : "))
luas_dinding = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
kaleng_cat = luas_dinding / 10
print("Luas dinding :", luas_dinding)
print("Kaleng cat yang dibutuhkan :", kaleng_cat)