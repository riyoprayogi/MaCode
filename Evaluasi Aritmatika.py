import sys
print("""*Program Mengevaluasi Aritmatika*""")
loop = -1
while loop < 0:
    print("Masukkan Perintah Aritmatika Sederhana")
    kal = input("")
    if "ditambah" in kal:
        kali = kal.replace(" ditambah ", ",")
        kalim = kali.split(",")
        kalimat_a = float(kalim[0])
        kalimat_b = float(kalim[1])
        kalimat = kalimat_a + kalimat_b
        print("Hasil Penjumlahannya yaitu :",kalimat)
        print()
    elif "dikurang" in kal:
        kali = kal.replace(" dikurang ", ",")
        kalim = kali.split(",")
        kalimat_a = float(kalim[0])
        kalimat_b = float(kalim[1])
        kalimat = kalimat_a - kalimat_b
        print("Hasil Pengurangannya yaitu :", kalimat)
        print()
    elif "dibagi" in kal:
        kali = kal.replace(" dibagi ", ",")
        kalim = kali.split(",")
        kalimat_a = float(kalim[0])
        kalimat_b = float(kalim[1])
        kalimat = kalimat_a / kalimat_b
        print("Hasil Pembagiannya yaitu :", kalimat)
        print()
    elif "dikali" in kal:
        kali = kal.replace(" dikali ", ",")
        kalim = kali.split(",")
        kalimat_a = float(kalim[0])
        kalimat_b = float(kalim[1])
        kalimat = kalimat_a * kalimat_b
        print("Hasil Perkaliannya yaitu :", kalimat)
        print()
    elif "selesai" in kal:
        sys.exit("Goodbye")
    else:
        print("Masukkan Operasi dengan benar")