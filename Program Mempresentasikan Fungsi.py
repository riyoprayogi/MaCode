# Program Rumus
def fungsi(x):
    if x<=-10 or x>=10 :
        print("\nnilai x harus bilangan bulat antara -10 sampai 10")
        fungsi(int(input("masukan nilai x | -10 > x > 10 :")))
    else:
        print("\ny = 6x\u00b2 + 3x + 2")
        print("y = 6(%d)\u00b2 + 3(%d) + 2" % (x,x))
        print("y =", 6*(x**2) + 3*x + 2)

fungsi(int(input("masukan nilai x | -10 > x > 10 :")))
