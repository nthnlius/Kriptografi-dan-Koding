#Kode ini adalah kode yang digunakan untuk menyelesaikan latihan One Time Pad yang diberikan pada saat kelas di slide
#One Time Pad pada halaman 14.
plaintext = "TLCYKUMGDFAWTZVOYKLENSZZHYZRW"
key1 = []
key2 = []
targettext1 = "MRJOHNSONLEFTHISHOUSELASTNIGHT"
targettext2 = "ISAWTHEMYSTERIOUSPLANEBEHINDME"
#key1 digunakan untuk mencari kunci pada Vigenere Cipher untuk mencari target targettext1
#key 2 digunakan untuk mencari targettext2
j = 0 # adalah index untuk menandai karakter ke j pada targettext1 dan targettext2
for char in plaintext:
    i = 0 #adalah index yang akan diiterasi untuk mencari kecocokan pada ASCII character untuk setiap karakter.
    ordchar = ord(char)
    ordtarget1 = ord(targettext1[j])
    ordtarget2 = ord(targettext2[j])
    ordhasil = (ordchar + i)
    while (ordhasil != ordtarget1):
        i = i+1
        ordhasil = ((ordchar + i -65)%26)
        ordhasil = ordhasil + 65
    key1.append(chr(i+65))

    i = 0
    ordkey = i
    ordhasil = (ordchar + ordkey)
    while (ordhasil != ordtarget2):
        i = i+1
        ordhasil = ((ordchar + i-65)%26)
        ordhasil = ordhasil + 65
    key2.append(chr(i+65))
    j = j+1

#berikut ini adalah kode yang digunakan untuk menampilkan key1 dan key2 ke layar untuk mendapatkan
#key yang dapat merubah plaintext menjadi targettext
for elmt in key1 :
    print(elmt, end = '') 
print()
for elmt in key2:
    print(elmt, end = '')
print ()