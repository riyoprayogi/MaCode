print(".::\033[31mPerkalian Matriks\033[30m::.")
print("""\033[34m
[a b] [e f]
[c d] [g h]
\033[30m""")
print("\033[32mMatriks 1\033[30m")
a = int(input("a: "))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
print('\033[32m\nMatriks 2\033[30m')
e = int(input('e: '))
f = int(input('f: '))
g = int(input('g: '))
h = int(input('h: '))
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
