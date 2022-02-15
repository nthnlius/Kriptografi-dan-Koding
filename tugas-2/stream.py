class RC4:
    def __init__(self, key: bytearray) -> None:
        self.__key = key
        self.__S = self.__KSA(bytearray([i for i in range(256)]))
    
    def __KSA(self, S: bytearray) -> bytearray:
        j = 0
        for i in range(255):
            j = (j + S[i] + ord(self.__key[i%len(self.__key)])) % 256
            S[i], S[j] = S[j], S[i]
        return S
    
    def __PRGA(self, message: bytearray) -> bytearray:
        i = 0
        j = 0
        C = []
        key = self.__S.copy()

        for i, m in enumerate(message):
            i = (i + 1) % 256
            j = (j + key[i]) % 256
            key[i], key[j] = key[j], key[i]
            t = (key[i] + key[j]) % 256
            u = key[t]
            c = m ^ self.__LFSR(key, u)
            C += [c]
        return bytearray(C)

    def encrypt(self, plaintext: bytearray) -> bytearray:
        return self.__PRGA(plaintext)
    
    def decrypt(self, ciphertext: bytearray) -> bytearray:
        return self.__PRGA(ciphertext)
    
    def __LFSR(self, key: bytearray, u: int) -> int:
        x = key.pop()
        out = x ^ u
        key.append(out)
        return out