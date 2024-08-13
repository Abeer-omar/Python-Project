from .CaesarCipher import CaesarCipherClass
#from CaesarCipher import CaesarCipherClass


defaultKey = {
    "a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
    "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", 
    "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", 
    "v": "y", "w": "z", "x": "a", "y": "b", "z": "c", " ": " ",
    "A": "D", "B": "E", "C": "F", "D": "G", "E": "H", "F": "I", "G": "J",
    "H": "K", "I": "L", "J": "M", "K": "N", "L": "O", "M": "P", "N": "Q", 
    "O": "R", "P": "S", "Q": "T", "R": "U", "S": "V", "T": "W", "U": "X", 
    "V": "Y", "W": "Z", "X": "A", "Y": "B", "Z": "C"
}

def get_cipher(string, encrypt=True, key=None):
    if key is None:
        key = defaultKey

    cipher = CaesarCipherClass(key)

    if encrypt:
        return cipher.encrypt_string(string)
    else:
        return cipher.decrypt_string(string)
 

