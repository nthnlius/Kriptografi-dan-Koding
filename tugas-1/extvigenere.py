##Pengolahan key
def key_generator(text):
    key = input("Masukkan key: ")

    i = 0
    while len(key) < len(text):
        key += key[i]
        i += 1

    return key


##Extended Vigenere
method = input("Enkripsi atau Dekripsi (E/D)? ")

while method.upper() != "Y":
    ##Enkripsi
    if method.upper() == "E":
        plain = input("Masukkan plaintext: ")
        plain.replace(" ", "")
        key = key_generator(plain)
        cipher = ""
        
        for i in range(len(plain)):
            cipher += chr((ord(plain[i]) + ord(key[i])) % 256)
        print(cipher)

    ##Dekripsi
    elif method.upper() == "D":
        cipher = input("Masukkan ciphertext: ")
        key = key_generator(cipher)
        plain = ""
        
        for i in range(len(cipher)):
            plain += chr((ord(cipher[i]) - ord(key[i])) % 256)
        print(plain)

    method = input("Stop (Y/N)? ")
    if method.upper() == "N":
        method = input("Enkripsi atau Dekripsi (E/D)?")