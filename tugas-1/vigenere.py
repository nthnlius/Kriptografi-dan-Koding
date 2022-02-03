from random import randrange
from telnetlib import ENCRYPT
import os.path
keyfile = "keyII4031Kirptografidankodingtapiadatypo.txt"
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

def otp(plain, enkripsi, keyfiles):
    #plain adalah plaintext yang akan di-cipher-kan
    #enkripsi adalah nilai boolean yang akan bernilai True jika pengguna ingin mengenkripsi
        # dan akan bernilai False jika pengguna ingin mendekripsi.
    if enkripsi :
        randomtext(len(plain))
        global keyfile
        with open(keyfile)as f:
            key = f.readline()
    else :
        key = keyfiles
    ciphertext = vigenere(plain, key, enkripsi)

    return ciphertext
def vigenere (plain, key, encrypt): 
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
        return text
    else : #pilihan mendekripsi
        text = ""
        for i in range (len(plain)):
            ordchar = ord(plain[i])
            if (ordchar>=65 and ordchar<=90):
                ordkey = ord(key[i%len(key)])
                ordhasil = (ordchar - ordkey)%26
                text += chr(ordhasil+65)
            else :
                text += chr(ordchar)
        return text

def extvigenere (plain, key, encrypt):
    res = ""
    if encrypt :
        res = bytes([((ord(x)+ord(key[i%len(key)]))%256)for i, x in enumerate(plain)])
    else :
        res = bytes([((ord(x)-ord(key[i%len(key)]))%256)for i, x in enumerate(plain)])
    return res