print(".::: Latihan Soal :::.")
print("\033[33m1. Gunakan TFK 1 untuk menyelesaikan soal ini !\n"
      "batas atas \t= x\n"
      "batas bawah = 1\n"
      "5(t) + t dt\033[0m")
jwb_tfk1 = str(input("Hasilnya adalah ... "))

if (jwb_tfk1 == "5(x) + x"):
    print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
    print("\033[33m2. Gunakan TFK 2 untuk menyelesaikan soal ini !\n"
          "Hitunglah nilai dari (3x^2 + 2x - 1) dx , dengan\n"
          "batas atas \t= 3\n"
          "batas bawah = 1\033[0m")
    jwb_tfk2 = str(input("Hasilnya adalah ... "))

    if (jwb_tfk2 == "32"):
        print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
        print("\033[33m3. Gunakan TFK 1 untuk menyelesaikan soal ini !\n"
              "Diketahui suatu fungsi f(x) = (t^4 + t - 1) , dengan\n"
              "batas atas \t= x\n"
              "batas bawah = -1\n"
              "Maka nilai dari f'(1) = ..., dengan f'(x) adalah turunan pertama dari fungsi f(x).\033[0m")
        jwb_tfk3 = str(input("Hasilnya adalah ... "))

        if(jwb_tfk3 == "1"):
            print("Jawaban Benar, Lanjut ke Soal Berikut nya ...\n")
            print("\033[33m4. Gunakan TFK 2 untuk menyekesaikan soal ini !\n"
                  "Diketahui suatu fungsi f(x) = x^2n , dengan\n"
                  "batas atas \t= 5\n"
                  "batas bawah = 2\033[0m")
            jwb_tfk4 = str(input("Maka hasilnya adalah ... "))

            if(jwb_tfk4 == "39"):
                print("Jawaban Benar, Lanjut ke Soal Terakhir ...\n")
                print("\033[33m5. Gunakan TFK 2 untuk menyelesaikan soal ini !\n"
                      "Hitunglah (3 - 2x + x^2) dx , dengan\n"
                      "batas atas \t= 3\n"
                      "batas bawah = 1\n"
                      "Gunakan ( / ) untuk jawaban pecahan\033[0m")
                jwb_tfk4 = str(input("Maka hasilnya adalah ... "))

                if (jwb_tfk4 == "20/3"):
                    print("Jawaban Benar, Selamat Kamu Telah Menyelesaikan Semua Latihan Soal\n")

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