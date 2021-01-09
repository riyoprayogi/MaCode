def harga_diskon(harga_asal, diskon):
    harga_diskon = harga_asal - (harga_asal * diskon / 100)
    return harga_diskon

harga = input("Masukkan harga: ")
harga = int(harga)
diskon = input("Masukkan diskon (tanpa persen/%): ")
diskon = float(diskon)

print("Harga diskon menjadi: ", harga_diskon(harga, diskon), "rupiah")