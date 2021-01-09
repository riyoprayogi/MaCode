def harga_diskon(harga_asal, diskon):
    harga_diskon = harga_asal - (harga_asal*diskon/100)
    return harga_diskon
harga = int(input("Masukkan harga: "))
assert harga >=50000, "Harga yang dimasukkan harus >= 50000. Silahkan masukan harga di atas 50000"
diskon = float(input("Masukkan diskon (tanpa persen/%): "))

print("Harga Aawal : ", harga)
print("Harga diskon menjadi: ", harga_diskon(harga, diskon), "rupiah")