def playfair (plaintext, key, enkripsi):
    globalkey = 'abcdefghiklmnopqrstuvwxyz'
    globalkey = globalkey.upper()
    listkey = []
    key = key.upper()
    for char in key :
        if (char not in listkey):
            if (char != 'J'):
                listkey.append(char)
    for char in globalkey :
        if (char not in listkey):
            listkey.append(char)
    # print(listkey)
    keysquare = [['A'for i in range (5)] for j in range (5)]
    strkey = ""
    for i in range (5):
        for j in range (5):
            keysquare[i][j] = listkey[i*5+j]
            strkey += listkey[i*5+j]    
        # print(keysquare)
    if enkripsi :
        plaintext.upper()
        plaintext.replace("J", "I")
        bigram = []
        i = 0
        while (i < len (plaintext)-1):
            if plaintext[i]== plaintext[i+1] :
                text = plaintext[i] + 'X'
                i+=1
                bigram.append(text)
            else :
                text = plaintext[i] + plaintext[i+1]
                i+=2
                bigram.append(text)
        if (i+1 == len (plaintext)):
            text = plaintext[i]+"X"
            bigram.append(text)
        finalbigram = []
        for couple in bigram :
            if is_same_row(couple[0], couple[1], strkey):
                text = strkey[(strkey.find(couple[0])+1)%5 + (strkey.find(couple[0])//5)*5] + strkey[(strkey.find(couple[1])+1)%5 + (strkey.find(couple[1])//5)*5]
                finalbigram.append(text)
            elif is_same_column(couple[0], couple[1], strkey):
                text = strkey[(strkey.find(couple[0])+5)%25] + strkey[(strkey.find(couple[1])+5)%25]
                finalbigram.append(text)
            else :
                i0 = strkey.find(couple[0])//5
                j0 = strkey.find(couple[0])%5
                i1 = strkey.find(couple[1])//5
                j1 = strkey.find(couple[1])%5
                text = strkey[i0*5 + j1] + strkey[i1*5 + j0]
                finalbigram.append(text)
        finaltext = ""
        for couple in finalbigram :
            finaltext = finaltext + couple[0]+couple[1]
        return finaltext
    else :
        bigram = []
        for i in range (0, len(plaintext), 2):
            text = plaintext[i]+ plaintext[i+1]
            bigram.append(text)
        finalbigram = []
        for couple in bigram :
            if (is_same_row(couple[0], couple[1], strkey)):
                character1 = strkey[(strkey.find(couple[0]) - 1)%5 + (strkey.find(couple[0])//5)*5]
                character2 = strkey[(strkey.find(couple[1])-1)%5 + (strkey.find(couple[0])//5)*5] 
                text = character1+character2
                del(character1)
                del(character2)
                finalbigram.append(text)
            elif (is_same_column(couple[0], couple[1], strkey)):
                character1 = strkey[(strkey.find(couple[0])-5)%25]
                character2 = strkey[(strkey.find(couple[1])-5)%25]
                text = character1 + character2
                del (character1)
                del (character2)
                finalbigram.append(text)
            else :
                i0 = strkey.find(couple[0])//5
                j0 = strkey.find(couple[0])%5
                i1 = strkey.find(couple[1])//5
                j1 = strkey.find(couple[1])%5
                text = strkey[i0*5 + j1] + strkey[i1*5 + j0]
                finalbigram.append(text)
        finaltext = ""
        for char in finalbigram:
            finaltext = finaltext + char[0]+char[1]
        return finaltext


def is_same_row (char1, char2, string):
    #fungsi digunakan untuk mencari apakah char1 dan char2 pada baris yang sama :
    return (string.find(char1)//5 == string.find(char2)//5)
def is_same_column (char1, char2, string):
    return (string.find(char1)% 5 == string.find(char2)%5)

