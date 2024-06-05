def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 26
            start = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - start - shift) % shift_amount + start)
        else:
            plaintext += char
    return plaintext


def root13_encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - shift_base + 13) % 26 + shift_base)
        else:
            ciphertext += char
    return ciphertext

def root13_decrypt(ciphertext):
    return root13_encrypt(ciphertext)


def vigenere_encrypt(plaintext, key):
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext.upper()]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        if chr(plaintext_int[i]).isalpha():
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        else:
            ciphertext += chr(plaintext_int[i])
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


def beaufort_encrypt(plaintext, key):
    key = key.upper()
    key_length = len(key)
    plaintext = plaintext.upper()
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i % key_length]) - 65
            if plaintext[i].isupper():
                shift_base = ord('A')
            else:
                shift_base = ord('a')
            value = (shift_base + 26 - (ord(plaintext[i]) - shift_base + shift) % 26)
            ciphertext += chr(value)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def beaufort_decrypt(ciphertext, key):
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (key_as_int[i % key_length] - ciphertext_int[i]) % 26
        plaintext += chr(value + 65)
    return plaintext


def autokey_encrypt(plaintext, key):
    key = key.upper()
    key_length = len(key)
    plaintext = plaintext.upper()
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - 65
            if char.isupper():
                shift_base = ord('A')
            else:
                shift_base = ord('a')
            value = (shift_base + (ord(char) - shift_base + shift) % 26)
            ciphertext += chr(value)
            key_index += 1
            key += char
        else:
            ciphertext += char
    return ciphertext

def autokey_decrypt(ciphertext, key):
    key = key.upper()
    key_length = len(key)
    ciphertext = ciphertext.upper()
    plaintext = ""
    key_index = 0

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key += decrypted_char
            key_index += 1
        else:
            plaintext += ciphertext[i]
    return plaintext
