'''
# test perulangan

# perulangan FOR
for i in range (10):
    print("Code ke-{}".format(i))

# perulangan FOR menggunakan string
variabel = "KULIAH di ITK nih"
for i in variabel:
    print(i)

# FOR pada list
code_tipe = ["C", "C++", "C#", "Python", "Java", "JavaScript"]
for i in code_tipe:
    print("Bahasa Pemrograman {}".format(i))

# Perulangan menggunakan While
i = 0
while i < 10**2:
    i+=1
    print(i)

# Infinte Loop
i = 1
while i < 10:
    print(i) # note:ctrl c

# Perulangan Bersarang
for baris in range(5):
    for kolom in range(baris+1):
        print(" * ", end="")
    print()
    
'''
