print(".:: Program Prediksi Investasi ::.\n")

saldo = int(input("Masukkan Saldo Awal (Rp.) : "))
persentase = float(input("Masukkan Persentase Keuntungan Per Tahunnya (%) : "))
tahun = int(input("Masukkan Waktu Investasi (Tahun) : "))

print("Tahun Ke-\t Saldo Awal\t\t Laba Investasi\t\t Saldo Akhir")

for i in range(tahun):
    laba = saldo*(persentase/100)
    saldoAkhir = saldo+laba
    print(f"\t{i}\t\t {round(saldo,2)}\t\t\t {round(laba,2)}\t\t\t{round(saldoAkhir,2)}")
    saldo = saldoAkhir
