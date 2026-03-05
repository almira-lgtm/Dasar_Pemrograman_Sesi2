harga_awal = float(input("Masukkan harga awal laptop : "))
nilai_sisa = float(input("Masukkan nilai sisa : "))
umur = int(input("Masukkan umur ekonomis (tahun) : "))
penyusutan_pertahun = (harga_awal - nilai_sisa) / umur
nilai_setelah_2tahun = harga_awal - (penyusutan_pertahun * 2)
print("=====Penyusutan Nilai Barang=====")
print("Penyusutan pertahun :", penyusutan_pertahun)
print("Nilai setelah 2 tahun :", nilai_setelah_2tahun)