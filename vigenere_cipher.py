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
