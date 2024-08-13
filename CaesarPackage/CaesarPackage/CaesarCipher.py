class CaesarCipherClass:
    def __init__(self, key):
        self.key = key
        self.antikey = {val:k for k,val in key.items()}   #changes values to keys and vice versa

    def check_input(self, string):
        if not all(letter.isalpha() or letter.isspace() for letter in string):
            raise ValueError("Invalid input: only alphabets and spaces are allowed.")
        
    def encrypt_string(self, string):
        self.check_input(string)
        encrypted_Str = ""

        for letter in string:
            encrypted_Str += self.key[letter]
        return encrypted_Str
     

    def decrypt_string(self, string):
        self.check_input(string)
        decrypted_Str = ""

        for letter in string:
            decrypted_Str += self.antikey[letter]
        return decrypted_Str
        
