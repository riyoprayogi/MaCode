print("""*Program Huruf Terbalik & Menghitung Huruf Vokal""")
kalimat = (input('Masukkan Kalimat: '))
assert kalimat.islower(),"Masukan Kalimat Bukan Angka"
total = 0
total = kalimat.count('a') + kalimat.count('i') + kalimat.count('u') \
        + kalimat.count('e') + kalimat.count('o')
print('Hasil Pembalikan Kalimat :', ''.join(reversed(kalimat)))
print('Jumlah Huruf Vokal Ada :', total)