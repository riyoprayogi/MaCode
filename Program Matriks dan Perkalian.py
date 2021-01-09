import sys
print(".::\033[31mProgram Pembuat Matriks\033[30m::.")
pil = -1
while (pil!= 3):
    print("\n\033[30m -Menu-")
    print("1. Pembuat matrix !!")
    print("2. Perkalian !!")
    print("3. matikan program !!")
    pil = int(input("Pilihan anda : "))
    if (pil == 1):
        print(".::\033[31mPembuat Matrix\033[30m::.")
        print ("""\033[34m
    00 01 02
    10 11 12
    20 21 22
    \033[30m""")

        a = input('\033[35mMasukkan jumlah baris : ')
        assert a.isdigit(),"Masukan berupa angka"
        a = int(a)
        b = input('Masukkan jumlah kolom : \033[30m')
        assert b.isdigit(),"Masukan berupa angka"
        b = int(b)
        print('')
        mat=[]
        for i in range(a):
            c=[]
            for j in range (b):
                j=input("\033[33mMasukkan nilai ! \033[30m"+str(i)+""+str(j)+"\033[33m" ": ")
                assert j.isdigit(),"Masukan berupa angka"
                j = int(j)
                c.append(j)
            mat.append(c)
        print("\033[31mmatriksnya adalah :\033[34m\n")
        for x in mat:
            print(x)

    if (pil == 2):
        print(".::\033[31mPerkalian Matriks\033[30m::.")
        print("""\033[34m
    [a b] [e f]
    [c d] [g h]
    \033[30m""")
        print("\033[32mMatriks 1\033[30m")
        a = input("a: ");assert a.isdigit(), "Masukan berupa angka"
        a = int(a)
        b = input("b: ");assert b.isdigit(), "Masukan berupa angka"
        b = int(b)
        c = input('c: ');assert c.isdigit(), "Masukan berupa angka"
        c = int(c)
        d = input('d: ');assert d.isdigit(), "Masukan berupa angka"
        d = int(d)
        print('\033[32m\nMatriks 2\033[30m')
        e = input('e: ');assert e.isdigit(), "Masukan berupa angka"
        e = int(e)
        f = input('f: ');assert f.isdigit(), "Masukan berupa angka"
        f = int(f)
        g = input('g: ');assert g.isdigit(), "Masukan berupa angka"
        g = int(g)
        h = input('h: ');assert h.isdigit(), "Masukan berupa angka"
        h = int(h)
        print(f"""\033[34m
        [{a} {b}] [{e} {f}]
        [{c} {d}] [{g} {h}]
        \033[30m""")
        mat1 = [
        [a, b],
        [c, d],
        ]
        mat2 = [
        [e, f],
        [g, h],
        ]
        mat3 = []
        for x in range(0, len(mat1)):
            row = []
            for y in range(0, len(mat1[0])):
                total = 0
                for z in range(0, len(mat1)):
                    total = total + (mat1[x][z] * mat2[z][y])
                row.append(total)
            mat3.append(row)
        print("\033[31mhasil perkaliannya adalah :\033[35m")
        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], end=' ')
            print()
    elif (pil == 3):
        sys.exit("program dimatikan...")