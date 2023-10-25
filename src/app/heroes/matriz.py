
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]


tamano = len(a)
colA = 0
filA = 0
colB = 0
filB = 0
colC = 0
filC = 0
contador = 0

for i in range(tamano):

    for i in range(tamano):

        x = a[filA][colA]
        y = b[filB][colB]
        contador = contador + x * y
        colA += 1
        filB += 1

    c[filC][colC] = contador
    colB += 1
    colC += 1
    x = 0
    y = 0


print(c)
