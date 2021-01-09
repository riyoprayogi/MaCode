def faktorial():
    i = int(input("Masukan nilai bilangan : "))
    assert i > 0,"Harus angka positif oke"
    sum = 1
    rumus = str(i) + "! = "
    while i > 1:
        sum = sum * i
        rumus += str(i) + " x "
        i = i - 1
    rumus += "1 ="
    print(rumus, sum)
faktorial()
