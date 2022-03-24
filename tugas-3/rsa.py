'''program ini diciptakan untuk mencoba melakukan enkripsi menggunakan RSA'''
from time import time
from math import ceil, floor, sqrt, gcd, log
from typing import Tuple
import sympy
import json
def isPrime(rndint) -> bool:
    if rndint>=10 :
        for i in range (2, ceil(sqrt(rndint))+1):
            if (rndint%i == 0):
                return False
        return True
    elif rndint >0 and rndint<10 :
        for i in range (2, rndint):
            if (rndint%i == 0):
                return False
        return True
    else :
        return isPrime((rndint)*(-1))
class RSA:
    def __init__(self):
        try :
            with open("RSA-NN.pub", "r")as r:
                pubkey = json.load(r)
                self.e = pubkey['e']
                self.n = pubkey['n']
            with open("RSA-NN.pri", "r")as r:
                prikey = json.load(r)
                self.d = prikey['d']
        except FileNotFoundError :
            p = sympy.randprime(2**63, 2**64-1)
            q = sympy.randprime(2**63, 2**64-1)
            while p==q :
                q = sympy.randprime(2**63, 2**64-1)
            self.n = p*q
            self.tot = (p-1)*(q-1)
            self.generateE()
            self.generateD()
            tup = {'d':self.d, 'n':self.n}
            with open("RSA-NN.pri" , "w")as f:
                json.dump(tup, f)
            tup = {'e':self.e, 'n':self.n}
            with open ("RSA-NN.pub", "w")as f:
                json.dump(tup, f)
    
    def isEallowed(self, e)-> bool:
        if (isPrime(self.p) and isPrime(self.q)):
            return gcd(e, self.tot) == 1
    def generateE(self)->None:
        randnum = sympy.randprime(2**63, 2**64-1)
        while (gcd(randnum, self.tot)!=1):
            randnum = sympy.randprime(2**63, 2**64-1)
        self.e = randnum
    ''' rumus : d = (1+k*tot)/e'''
    def setE(self,num):
        if (self.isEallowed(num)):
            self.e=num
            print ("E has been set")
        else :
            print("You have chosen the wrong E")

    def generateD(self)-> int:
        d = pow(self.e, -1, self.tot)
        print("d has been set to : ", d)
        self.d = d
        return d
    def encrypt(self, message:bytearray):
        ciphertext = []
        print("encrypting message : ", message)
        for byt in message :
            byte = ord(byt)
            # print (byte)
            ciphermsg = pow(byte, self.e, self.n)
            ciphertext.append(ciphermsg)
        return ciphertext
    def decrypt (self, ciphermsg : bytearray):
        plaintext = []
        plaintxt = ''
        # for byte in ciphermsg:
        #     plainmsg = (pow(byte, self.d, self.n))
        #     plaintext.append(plainmsg)
        for i in range (0, len(ciphermsg)//32, 32):
            # print (ciphertext[i])
            text9 = ciphertext[i*32:i*32+32]
            # print("text : ", text9)
        for i in range (len(text9)):
            plainmsg = pow(text9[i], self.d, self.n)
            plaintext.append(plainmsg)
            plaintxt+=chr(plainmsg)
        print (plaintxt)
        
        return (plaintext)

def nextPrime(x):
    nextprime = x + 1
    while (not isPrime(nextprime)):
        print(nextprime, "is not a prime number")
        nextprime +=1
    print(nextprime, "is prime number")
    return nextprime

def isEven(x : int)->bool :
    return x%2==0
def exp2(a:int , b:int)-> int :
    if b == 0:
        return 1
    else :
        x = exp2(a, b//2)
        if (isEven(b)):
            return x*x
        else :
            return x*x*a
rsa = RSA()
plaintext = "ASU" #19
print ("panjang plaintext : ",len(plaintext))
ciphertext = rsa.encrypt(plaintext)
nani = ""
check=[]
for i in range (len (ciphertext)):
    text = hex(ciphertext[i])
    if (len(text)< 34):
        # print (text[0:2])
        text2 = text[0:2]+('0'*(34-len(text)))+text[2:len(text)]
    else :
        text2 = text
    for j in range (1, len(text2)//2):
        euy = text2[j*2 :j*2+2] #euy mengambil tiap bytes dalam text.
        ahh = int(euy, 16) #ahh mengubah euy dari heksadesimal jadi integer
        nani+=(chr(ahh))
        check.append(ahh)
    # print ("len2 : ", len(text2))
    # print (" text2 : ", text2)
    
enc = bytearray(nani, encoding = "iso8859")
filename = "main.py"
f = open(filename, "wb")
f.write(enc)

f = open(filename, "rb")
dec = f.read()
decs = bytearray(dec)
plntxt = rsa.decrypt(decs)
# print (plntxt)