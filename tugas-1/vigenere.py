from random import randrange
from telnetlib import ENCRYPT
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

def otp(plain, enkripsi, group):
    #plain adalah plaintext yang akan di-cipher-kan
    #enkripsi adalah nilai boolean yang akan bernilai True jika pengguna ingin mengenkripsi
        # dan akan bernilai False jika pengguna ingin mendekripsi.
    if enkripsi :
        randomtext(len(plain))
    global keyfile
    with open(keyfile)as f:
        key = f.readline()
    ciphertext = vigenere(plain, key, enkripsi, group)

    return ciphertext
def vigenere (plain, key, encrypt, group): 
    #plain adalah plaintext
    #key adalah kuncinya
    #encrypt adalah boolean. True jika akan mengenkripsi, false jika akan mendekripsi
    plain = plain.upper()
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
        if group :
            ciphertext1 = '' + text[0]
            for i in range (1, len(text)):
                if i%5==0 :
                    ciphertext1+=" "
                ciphertext1+=text[i]
            text = ciphertext1
        return text
    else : #pilihan mendekripsi
        text = ""
        for i in range (len(plain)):
            ordchar = ord(plain[i])
            ordkey = ord(key[i%len(key)])
            ordhasil = (ordchar - ordkey)%26
            text += chr(ordhasil+65)
        return text

def extvigenere (plain, key, encrypt):
    res = ""
    if encrypt :
        res = bytes([((ord(x)+ord(key[i%len(key)]))%256)for i, x in enumerate(plain)])
    else :
        res = bytes([((ord(x)-ord(key[i%len(key)]))%256)for i, x in enumerate(plain)])
    return res

print(otp ("thisplaintext", True, True))