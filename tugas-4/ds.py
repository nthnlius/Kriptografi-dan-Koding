from rsa import *
import hashlib

def sign_function(input, key, n, terpisah):
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
    if terpisah :
        with open(output, 'w') as f:
            f.write(full_sign)
            f.close()
    else :
        with open(output, 'w') as f:
            f.write(msg+'\n'+full_sign)
            f.close()


def verify_function(inputfile, key, n, inputsign=None):
    
    rsa = RSA()
    opening_text = "*** Begin of digital signature ****\n"
    ending_text = "\n*** end of digital signature ****\n"
    if inputsign != None :
        with open(inputsign, 'r') as signature:
            sign = signature.read()
        a = sign.find(opening_text)
        b = sign.find(ending_text)
        hexcode = sign[a+len(opening_text) : b]
        hexsign = int(hexcode, 16)
        with open(inputfile, 'r') as f:
            msg = f.read()
        new_hash = int(hashlib.sha1(msg.encode()).hexdigest(), 16)
    else :
        with open(inputfile, 'r') as f:
            msg = f.read()
        a = msg.find(opening_text)
        b = msg.find(ending_text)
        # print ("a : ", a)
        # print ("b : ", b)
        # print ("len opening : ", len(opening_text))
        # print ("len ending : ", len(ending_text))
        # print ("len message : ", len(msg))

        #extract message + hash
        msgasli = msg[0:a-1].encode()
        print("msgasli: ", msgasli)
        new_hash = int(hashlib.sha1(msgasli).hexdigest(), 16)

        #extract sign
        hexcode = msg[a+len(opening_text):b]
        hexsign = int(hexcode, 16)
    print("hexsign : ", hexsign)
    print ("hexcode: ",hexcode)
    # print(msgasli)
    rsa.d = int(key)
    rsa.n = int(n)
    decrypted = rsa.decrypt(hexsign)

    print("decrypted: ", decrypted)
    print("newhash: ", new_hash)
    #verify
    if (decrypted == new_hash):
        output = "Verified!"
    else:
        output = "The file has been changed!"
    print("result: ", output)
    return output





# inputs = "encrypted.txt"
# filez = "encrypted.ds"
# prikey = 7129805958236125393909738899866134989728638063622359947119881565798251094414567045921221055364743742709033116352607338950617399946263110118790752194024153
# pubkey = 109558181538109078287528220891604334756710284053597150924934634686015175723113
# n = 7372594836593511881892902850168856802932406183893917829802923640246956366562853741765096072098940947314465379540487401549291738430994906582113728211934241
# sign_function(inputs, prikey, n)
# verify_function(filez, pubkey, n)