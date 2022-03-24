'''program ini diciptakan untuk mencoba melakukan enkripsi menggunakan RSA'''
from time import time
from math import ceil, floor, sqrt, gcd, log
from typing import Tuple
import sympy
import sys
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

        for byt in message :
            byte = byt
            # print (byte)
            ciphermsg = pow(byte, self.e, self.n)
            ciphertext.append(ciphermsg)
        print (ciphertext)
        # for i in range (len(ciphertext)):
            # print (hex(ciphertext[i]))
        return ciphertext
    def decrypt (self, ciphermsg : bytearray):
        plaintext = []
        plaintxt = ''
        print(len(ciphermsg))
        for i in range (0, len(ciphermsg), 16):
            print ("i :", i)
            print ("ciphermsg : ", ciphermsg)
            ciphertext = bytearray(ciphermsg)
            # print(type(ciphertext)) mengeluarkan bytearray
            text9 = int.from_bytes(ciphertext[i:i+16], byteorder="big", signed=False)
            # print ("aaa" , ciphertext[i*16:i*16+16])
            print(f'hex: {hex(text9)}')
            print("text : ", text9)
            # for j in range (len(text9)):
            plainmsg = pow(text9, self.d, self.n)
            print("plainmsg : ", plainmsg)
            plaintext.append(plainmsg)
            plaintxt+=chr(plainmsg)
        print (plaintxt)
        
        return (plaintxt)

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

# rsa=RSA()
# fileName = "/home/hydroxideacid/kuliah/kripto/tugas/tugas-3/output"
# with open("ASU.txt", "rb") as f :
#     fileraw = f.read()
# ciphertext = rsa.encrypt(fileraw)
# nani = ""
# check=[]
# for i in range (len (ciphertext)):
#     text = hex(ciphertext[i])
#     if (len(text)< 34):
#         # print (text[0:2])
#         text2 = text[0:2]+('0'*(34-len(text)))+text[2:len(text)]
#     else :
#         text2 = text
#     for j in range (1, len(text2)//2):
#         euy = text2[j*2 :j*2+2] #euy mengambil tiap bytes dalam text.
#         ahh = int(euy, 16) #ahh mengubah euy dari heksadesimal jadi integer
#         nani+=(chr(ahh))
#         check.append(ahh)
# with open(fileName, "rb") as f:
#     file = f.read()
# ciphertext = rsa.decrypt(file)
#72074772781006188336026735860538711311
#72074772781006188336062764657557675279
#0x363918a7fe74fc1f3b20f0695cec9d0f