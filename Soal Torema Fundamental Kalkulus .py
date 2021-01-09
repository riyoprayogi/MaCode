print(".::: Latihan Soal :::.")

def soal_kedua():
    print("\033[33m2. Gunakan TFK 2 untuk menyelesaikan soal ini !\n"
          "Hitunglah nilai dari (3x^2 + 2x - 1) dx , dengan\n"
          "batas atas \t= 3\n"
          "batas bawah = 1"
          "Hasilnya adalah ...\n"
          "\ta. 42\n"
          "\tb. 23\n"
          "\tc. 32\n"
          "\td. 33\033[0m\n")

def soal_ketiga():
    print("\033[33m3. Gunakan TFK 1 untuk menyelesaikan soal ini !\n"
          "Diketahui suatu fungsi f(x) = (t^4 + t - 1) , dengan\n"
          "batas atas \t= x\n"
          "batas bawah = -1\n"
          "Maka nilai dari f'(1) = ..., dengan f'(x) adalah turunan pertama dari fungsi f(x).\n"
          "\ta. 4\n"
          "\tb. 3\n"
          "\tc. 2\n"
          "\td. 1\033[0m\n")

def soal_keempat():
    print("\033[33m4. Gunakan TFK 2 untuk menyekesaikan soal ini !\n"
          "Diketahui suatu fungsi f(x) = x^2n , dengan\n"
          "batas atas \t= 5\n"
          "batas bawah = 2\n"
          "Hasilnya adalah ...\n"
          "\ta. 38\n"
          "\tb. 58\n"
          "\tc. 34\n"
          "\td. 39\033[0m\n")

def soal_kelima():
    print("\033[33m5. Gunakan TFK 2 untuk menyelesaikan soal ini !\n"
          "Hitunglah (3 - 2x + x^2) dx , dengan\n"
          "batas atas \t= 3\n"
          "batas bawah = 1\n"
          "Hasilnya adalah ...\n"
          "\ta. 20/3\n"
          "\tb. 20/5\n"
          "\tc. 10/3\n"
          "\td. 20/6\033[0m\n")

def total_score():
    total = 0
    total = s1 + s2 + s3 + s4 + s5
    print("Score Anda :", total)

print("\033[33m1. Gunakan TFK 1 untuk menyelesaikan soal ini !\n"
      "batas atas \t= x\n"
      "batas bawah = 1\n"
      "5(t) + t dt"
      "Hasilnya adalah ...\n"
      "\ta. 5(x) + x\n"
      "\tb. 5(t) + t\n"
      "\tc. 5/2(x) + t\n"
      "\td. 5/2(t) + t\033[0m\n")
jwb_tfk1 = str(input("Jawaban : "))

if (jwb_tfk1 == "a"):
    print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
    s1 = 20
    soal_kedua()
    jwb_tfk2 = str(input("Jawaban : "))

    if (jwb_tfk2 == "c"):
        print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
        s2 = 20
        soal_ketiga()
        jwb_tfk3 = str(input("Jawaban : "))

        if (jwb_tfk3 == "d"):
            print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
            s3 = 20
            soal_keempat()
            jwb_tfk4 = str(input("Jawaban : "))

            if (jwb_tfk4 == "d"):
                print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
                s4 = 20
                soal_kelima()
                jwb_tfk5 = str(input("Jawaban : "))

                if (jwb_tfk5 == "a"):
                    print("Jawaban Benar, Selamat Anda Telah Menyelesaikan Semua Soal ...")
                    s5 = 20
                    total_score()

                else:
                    print("Jawaban Anda Kurang Tepat, Baca Materi Kembali ...\n"
                          "Atau Coba Kerjakan Kembali Latihan Soal ...")

            else:
                print("Jawaban Anda Kurang Tepat, Baca Materi Kembali ...\n"
                      "Atau Coba Kerjakan Kembali Latihan Soal ...")

        else:
            print("Jawaban Anda Kurang Tepat, Baca Materi Kembali ...\n"
                  "Atau Coba Kerjakan Kembali Latihan Soal ...")

    else:
        print("Jawaban Anda Kurang Tepat, Baca Materi Kembali ...\n"
              "Atau Coba Kerjakan Kembali Latihan Soal ...")

else:
    print("Jawaban Anda Kurang Tepat, Baca Materi Kembali ...\n"
          "Atau Coba Kerjakan Kembali Latihan Soal ...")