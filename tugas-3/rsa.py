'''program ini diciptakan untuk mencoba melakukan enkripsi menggunakan RSA'''
from time import time
from math import ceil, floor, sqrt, gcd, log
from typing import Tuple
import sympy
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
    def __init__(self, p : int, q:int):
        self.p = p
        self.q = q
        self.e = 0
        self.d = 0
        self.n = self.p*self.q
        self.tot = (self.p-1) * (self.q-1)
    
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
        start_time = time()
        print("encrypting message : ", message)
        for byt in message :
            byte = ord(byt)
            # print (byte)
            ciphermsg = pow(byte, self.e, self.n)
            ciphertext.append(ciphermsg)
        end_time=time()
        print("Time taken for encrypting : ", (end_time - start_time), "seconds")
        return ciphertext
    def decrypt (self, ciphermsg : bytearray):
        plaintext = []
        start_time = time()
        for byte in ciphermsg:
            plainmsg = (pow(byte, self.d, self.n))
            plaintext.append(plainmsg)
        end_time=time()
        print("Time taken for decrypting : ", (end_time - start_time), "seconds")
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

rsa1 = RSA(sympy.randprime(2**63, 2**64-1), sympy.randprime(2**63, 2**64-1))
rsa1.generateE()
rsa1.generateD()
print (rsa1.e)
print(rsa1.d)
print(rsa1.n)
print(rsa1.tot)
ciphertext = rsa1.encrypt("yaolo")
nani = ''
check =[]
f = open("encrypted.txt", "wb")
# enc = bytearray(ciphertext)
for i in range (len (ciphertext)):
    text = hex(ciphertext[i])
    print (text)
    for j in range (1, len(text)//2):
        euy = text[j*2 :j*2+2] #euy mengambil tiap bytes dalam text.
        ahh = int(euy, 16) #ahh mengubah euy dari heksadesimal jadi integer
        nani+=(chr(ahh))
        check.append(ahh)
    
enc = bytearray(nani, encoding = "iso8859")
# for ii in range (len(check)):
    # print (hex(check[ii]))
f.write(enc)
    # print (euy)
    # hexad = text[2:4]
    # print(type(euy))
    # for i in range (2, len(text), 2):
    #     nani = byte()