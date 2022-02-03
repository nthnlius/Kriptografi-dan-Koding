#kode ini diadaptasi dari https://github.com/ScienceKot/Enigma/blob/master/enigma.py
from string import ascii_uppercase
alphabet = list(ascii_uppercase)
reflector = []
def permutate(rotor):
        ''' This function is permutatting the alphabet depending on the rotors settings '''
        global alphabet
        new_alphabet = ''.join(alphabet)
        new_alphabet = list(new_alphabet)
        alphabet = list(ascii_uppercase)
        for iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        return new_alphabet
def inverse_permutation(rotor):
        ''' This function is permutatting the alphabet depending on the rotors settings on the back way '''
        global alphabet
        new_alphabet = ''.join(alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.append(new_alphabet[0])
            new_alphabet.pop(0)
        return new_alphabet

def enigma (alphaasc, betaasc, gamaasc, text, enkripsi):
    global alphabet
    global reflector
    alpha = ord(alphaasc)-65
    beta = ord(betaasc)-65
    gama = ord(gamaasc)-65
    steckerbrett = {"" : ""}
    for letter in list(steckerbrett.keys()):
        if letter in alphabet:
            alphabet.remove(letter)
            alphabet.remove(steckerbrett[letter])
            steckerbrett.update({steckerbrett[letter]:letter})
        # Setting the reflector
    reflector = [leter for leter in reversed(alphabet)]
    ''' This function encrypts a string '''
    encrypted_text = []
    # Text preprocessing
    text = text.upper()
    text.split()
    # Encryption of every letter
    for letter in text:
        # Checking if the letter is in steckerbrett
        if letter not in alphabet :
            # encrypted_text.append(letter)
            pass
        else :
            if letter in steckerbrett:
                # If it is, the we encrypt it as it's pair
                encrypted_text.append(steckerbrett[letter])
                # Turning the rotors
                alpha += 1
                if alpha % len(alphabet) == 0:
                    beta += 1
                    alpha = 0
                if beta % len(alphabet) == 0 and alpha % len(alphabet) != 0 and beta >= len(
                        alphabet) - 1:
                    gama += 1
                    beta = 1
            else:
                # Encrypting throw rotors
                # Letter is encrypted by first rotor
                temp_letter = permutate(alpha)[alphabet.index(letter)]
                # Letter is encrypted by second rotor
                temp_letter = permutate(beta)[alphabet.index(temp_letter)]
                # Letter is encrypted by third rotor
                temp_letter = permutate(gama)[alphabet.index(temp_letter)]
                # Reflector is returning the inverse of that letter
                temp_letter = reflector[alphabet.index(temp_letter)]
                # Back way
                # Letter is encrypted by third rotor
                temp_letter = inverse_permutation(gama)[alphabet.index(temp_letter)]
                # Letter is encrypted by second rotor
                temp_letter = inverse_permutation(beta)[alphabet.index(temp_letter)]
                # Letter is encrypted by first rotor
                temp_letter = inverse_permutation(alpha)[alphabet.index(temp_letter)]
                encrypted_text.append(temp_letter)
                # turning the rotors
                alpha += 1
                if alpha % len(alphabet) == 0:
                    beta += 1
                    alpha = 0
                if beta % len(alphabet) == 0 and alpha % len(alphabet) != 0 and beta >= len(
                        alphabet) - 1:
                    gama += 1
                    beta = 1
    return ''.join(encrypted_text)

# text = "ABCDE123.FGHIJ456/KLMNO789,"

# print(enigma(5,17,24, text, True))
    