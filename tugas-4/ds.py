from rsa import *
import hashlib

def sign_function(input, key, n):
        with open(input, 'rb') as f:
            byte = f.read()

        doc_hash = int(hashlib.sha1(byte).hexdigest(), 16)
        print("hasil hash awal: ", doc_hash)

        rsa = RSA()
        rsa.e = int(key)
        rsa.n = int(n)
        encrypted = rsa.encrypt(doc_hash)
        print("encrypted : ", encrypted)
        # print(hex(encrypted))
        opening_text = "*** Begin of digital signature ****\n"
        sign = hex(encrypted)[2:len(hex(encrypted))]
        ending_text = "\n*** end of digital signature ****\n"
        full_sign = opening_text + sign + ending_text
        with open (input, 'r') as read:
            msg = read.read()
        output = input[0:len(input)-4]+'.ds'
        with open(output, 'w') as f:
            f.write(full_sign+msg)
            f.close()


def verify_function(input, key, n):
    rsa = RSA()
    opening_text = "*** Begin of digital signature ****\n"
    ending_text = "\n*** end of digital signature ****\n"
    with open(input, 'r') as f:
        msg = f.read()
    a = msg.find(opening_text)
    b = msg.find(ending_text)
    print ("a : ", a)
    print ("b : ", b)
    print ("len opening : ", len(opening_text))
    print ("len ending : ", len(ending_text))
    print ("len message : ", len(msg))

    #extract message + hash
    msgasli = msg[b+len(ending_text):len(msg)].encode()
    new_hash = int(hashlib.sha1(msgasli).hexdigest(), 16)

    #extract sign
    hexcode = msg[a+len(opening_text):b]
    hexsign = int(hexcode, 16)
    print("hexsign : ", hexsign)
    print ("hexcode: ",hexcode)
    print(msgasli)
    rsa.d = int(key)
    rsa.n = int(n)
    decrypted = rsa.decrypt(hexsign)

    print("decrypted: ", decrypted)
    print("newhash: ", new_hash)
    #verify
    if (decrypted == new_hash):
        output = "verified"
    else:
        output = "the file has been changed"
    print(output)




rsa= RSA()
rsa.genKey()
inputs = "encrypted.txt"
filez = "encrypted.ds"
prikey = 140251325155609021573677592164244666043
pubkey = 10487022383977417307
n = 153747857707562312388631452372614920519
sign_function(inputs, prikey, n)
verify_function(filez, pubkey, n)