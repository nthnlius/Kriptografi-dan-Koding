##Fungsi Pembuatan Key Matrix
def key_mtx(key):
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
    
    return matrix


##Fungsi Playfair
def playfair(enkripsi, key, input):
        
    matrix = key_mtx(key)
    
    input = input.replace(" ", "")
    input = input.upper()
    
    if enkripsi:
        input = input.replace("J", "I")

        done = False
        c = 0
        while not done:
            if c >= len(input) - 1:
                done = True
            else:
                if input[c] == input[c+1]:
                    input = input[:c+1] + 'X' + input[c+1:]
                c += 2

        if (len(input) % 2) == 1:
            input = input + 'X'

    c = 0
    output = ""

    while c < len(input):
        i1 = 0
        j1 = 0
        i2 = 0
        j2 = 0
        found1 = False
        found2 = False

        while (found1 and found2) is False: 
            for i in range(5):
                for j in range(5):
                    if (found1 and found2) is False:
                        if matrix[i][j] == input[c]:
                            i1 = i
                            j1 = j
                            found1 = True
                        elif matrix[i][j] == input[c+1]:
                            i2 = i
                            j2 = j
                            found2 = True

        if i1 == i2:
            if enkripsi:
                output += matrix[i1][(j1+1) % 5]
                output += matrix[i2][(j2+1) % 5]
            else:
                output += matrix[i1][(j1-1) % 5]
                output += matrix[i2][(j2-1) % 5]
        elif j1 == j2:
            if enkripsi:
                output += matrix[(i1+1) % 5][j1]
                output += matrix[(i2+1) % 5][j2]
            else:
                output += matrix[(i1-1) % 5][j1]
                output += matrix[(i2-1) % 5][j2]
        else:
            output += matrix[i1][j2]
            output += matrix [i2][j1]

        c += 2

    return output


##Pilih enkripsi atau dekripsi
method = input("Pilih enkripsi atau dekripsi (E/D): ")

stop = False
while not stop:
    ##Enkripsi:
    if (method.upper() == "E"):
        pt = input("Masukkan plaintext: ")        
        key = input("Masukkan key: ")
        ct = playfair(True, key, pt)
        print(ct)

    ##Dekripsi:
    elif (method.upper() == "D"):
        ct = input("Masukkan ciphertext: ")        
        key = input("Masukkan key: ")
        pt = ""
        pt = playfair(False, key, ct)
        print(pt)

    stp = input("Stop (Y/N)? ")
    if (stp.upper() == "Y"):
        stop = True
    else:
        method = input("Pilih enkripsi atau dekripsi (E/D): ")