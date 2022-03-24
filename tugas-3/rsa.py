'''program ini diciptakan untuk mencoba melakukan enkripsi menggunakan RSA'''
from time import time
from math import ceil, floor, sqrt, gcd, log
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
        return None
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
        if (isPrime(self.p) and isPrime(self.q)):
            
            tot = (self.p-1)*(self.q-1)
            count = 0
            i=10**(len(str(self.tot))-1)
            print ("=====================================================")
            print ("This is the allowed e : ")
            while (count < 50 and i < self.p*self.q):
                print (i)
                if(self.isEallowed(i)):
                    count +=1
                    print (i)
                i +=1
            print ("====================================================")
    ''' rumus : d = (1+k*tot)/e'''
    def setE(self,num):
        if (self.isEallowed(num)):
            self.e=num
            print ("E has been set")
        else :
            print("You have chosen the wrong E")

    def generateD(self)-> int:
        if (self.isEallowed(self.e)):
            d = pow(self.e, -1, self.tot)
            print("d has been set to : ", d)
            self.d = d
            return d
        else :
            print("no d has been set")
            return 0
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
