# Program Bilangan Prima
def prima(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "bukan bilangan prima")
                print(i, "kali", num//i, "=", num)
                break
            else:
                print(num,"adalah bilangan prima")
                break
    else:
        print(num, "bukan bilangan prima")
num = input("Masukkan nilai : ")
assert num.isdigit(),"Masukan berupa angka"
num = int(num)
prima(num)
