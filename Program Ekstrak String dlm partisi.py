angka="0123456789"
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym="+-@$()*/':#,=!?[]{}<>&_%√|¦\¤~¥°`...€$¥£¢₹₦¤ΦπΠ™©®^Δβα;«»¡¿"
def elemen(a):
    b=[];c=[];d=[];e=[]
    for i in range(len(a)):
        if a[i] in angka:
            b.append(a[i])
        elif a[i] in alp:
            c.append(a[i])
        elif a[i] in sym:
            d.append(a[i])
    e.append("".join(c))
    e.append("".join(b))
    e.append("".join(d))
    print(e)
elemen(input("masukan elemen : "))
