# BATAS
def hasil(a,b,c,d):
    if a>b:
        print("\nnilai batas bawah tidak boleh lebih besar dari nilai batas atas\n")
        hasil(int(input("masukan nilai batas bawah : ")),int(input("masukan nilai batas atas : ")),0,[])
    else:
        if a%2!=0:
            a=a+1
        d.append(str(a))
        c+=a
        if a<b-1:
            a+=2
            hasil(a,b,c,d)
        else:
            print("jumlah :", c, "didapat dari", "+".join(d))
hasil(int(input("masukan nilai batas bawah : ")),int(input("masukan nilai batas atas : ")),0,[])