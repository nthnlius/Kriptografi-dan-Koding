##Pembuatan Key Matrix
from sqlalchemy import false


key = input("Masukkan key: ")
key = key.replace(" ", "")
key = key.upper()

keylist = list()
for x in key:
    if x not in keylist:
        if x != 'J':
            keylist.append(x)

for i in range(65, 91):
    if chr(i) not in keylist:
        if chr(i) != 'J':
            keylist.append(chr(i))

matrix = [[0 for i in range(5)] for i in range(5)]
id = 0
for i in range(5):
    for j in range(5):
        matrix[i][j] = keylist[id]
        id += 1

print(matrix)



##Pengolahan plaintext
pt = input("Masukkan plaintext: ")
pt = pt.replace(" ", "")
pt = pt.upper()
pt = pt.replace("J", "I")

done = False
c = 0
while not done:
    if c >= len(pt) - 1:
        done = True
    else:
        if pt[c] == pt[c+1]:
            pt = pt[:c+1] + 'X' + pt[c+1:]
        c += 2

if (len(pt) % 2) == 1:
    pt = pt + 'X'

##Enkripsi
c = 0
cipher = ""

while c < len(pt):
    i1 = 0
    j1 = 0
    i2 = 0
    j2 = 0
    found1 = False
    found2 = False
    
    while found1 or found2 is False: 
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == pt[c]:
                    i1 = i
                    j1 = j
                    found1 = True
                    break
                elif matrix[i][j] == pt[c+1]:
                    i2 = i
                    j2 = j
                    found2 = True
                    break
    
    if i1 == i2:
        cipher += matrix[i1][j1+1 % 5]
        cipher += matrix[i2][j2+1 % 5]
    elif j1 == j2:
        cipher += matrix[i1+1 % 5][j1]
        cipher += matrix[i2+1 % 5][j2]
    else:
        cipher += matrix[i1][j2]
        cipher += matrix [i2][j1]
    
    c += 2

print(cipher)