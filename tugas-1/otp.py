from random import randrange
keyfile = "key.txt"
mode = "w"
def randomtext(length):
    #untuk membangkitkan sebuah text file dengan
    #isi random text untuk One Time Pad cipher
    global keyfile
    global mode
    test = ""
    randkey = []
    for i in range (length):
        a = chr(randrange(65,91))
        randkey.append(a)
        test += a

    with open(keyfile, mode) as f:
        f.write(test)

def otp(plain, enkripsi):
    #plain adalah plaintext yang akan di-cipher-kan
    #enkripsi adalah nilai boolean yang akan bernilai True jika pengguna ingin mengenkripsi
        # dan akan bernilai False jika pengguna ingin mendekripsi.
    if enkripsi :
        randomtext(len(plain))
    global keyfile
    with open(keyfile)as f:
        key = f.readline()
    ciphertext = vigenere(plain, key, enkripsi)
    return ciphertext
def vigenere (plain, key, encrypt): 
    #plain adalah plaintext
    #key adalah kuncinya
    #encrypt adalah boolean. True jika akan mengenkripsi, false jika akan mendekripsi
    key = key.upper()
    if encrypt :#pilihan mengenkripsi
        text = ""
        for i in range (len(plain)):
            ordchar = ord(plain[i])
            if (ordchar >=65 and ordchar <= 90):
                idxkey = i%len(key)
                ordkey = ord(key[idxkey])
                ordhasil = (ordchar - 65 + ordkey - 65)%26 + 65
                
                text += chr(ordhasil)
            else :
                text+=chr(ordchar)
        return text
    else : #pilihan mendekripsi
        text = ""
        for i in range (len(plain)):
            ordchar = ord(plain[i])
            ordkey = ord(key[i%len(key)])
            ordhasil = (ordchar - ordkey)%26
            text += chr(ordhasil+65)
        return text
