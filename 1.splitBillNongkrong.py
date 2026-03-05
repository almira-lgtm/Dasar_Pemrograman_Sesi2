total_tagihan = float(input("Masukkan Total tagihan : "))
total_orang = int(input("Masukkan total orang : "))
total_setelah_diberi_pajak = total_tagihan + (total_tagihan * 0.10)
total_bayar_perorang = total_setelah_diberi_pajak / total_orang
print("====Split Bill Bosss====")
print("Total Setelah Pajak: ",total_setelah_diberi_pajak)
print("Total Bayar Perorang: ",total_bayar_perorang )
