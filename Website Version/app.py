from flask import Flask, render_template, request, redirect, url_for, flash
import type_cipher

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        plaintext = request.form['input_text'].replace(" ", "")
        method = request.form['method']
        key = request.form['key'].replace(" ", "")

        if method == "Caesar Cipher":
            if not key.isdigit():
                flash("Kunci untuk Caesar Cipher harus berupa angka.")
                return redirect(url_for('encrypt'))
            shift = int(key)
            result = type_cipher.caesar_encrypt(plaintext, shift)
        elif method == "Root 13 Cipher":
            if key:
                flash("Root 13 Cipher tidak membutuhkan kunci. Kunci akan diabaikan.")
            result = type_cipher.root13_encrypt(plaintext)
        elif method == "Vigenere Cipher":
            if not key.isalpha():
                flash("Kunci untuk Vigenere Cipher harus berupa huruf.")
                return redirect(url_for('encrypt'))
            result = type_cipher.vigenere_encrypt(plaintext, key)
        elif method == "Beaufort Cipher":
            if not key.isalpha():
                flash("Kunci untuk Beaufort Cipher harus berupa huruf.")
                return redirect(url_for('encrypt'))
            result = type_cipher.beaufort_encrypt(plaintext, key)
        elif method == "Autokey Cipher":
            if not key.isalpha():
                flash("Kunci untuk Autokey Cipher harus berupa huruf.")
                return redirect(url_for('encrypt'))
            result = type_cipher.autokey_encrypt(plaintext, key)
        else:
            flash("Pilih metode enkripsi.")
            return redirect(url_for('encrypt'))

        return render_template('encrypt.html', result=result, method=method, input_text=plaintext, key=key)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        ciphertext = request.form['input_text'].replace(" ", "")
        method = request.form['method']
        key = request.form['key'].replace(" ", "")

        if method == "Caesar Cipher":
            if not key.isdigit():
                flash("Kunci untuk Caesar Cipher harus berupa angka.")
                return redirect(url_for('decrypt'))
            shift = int(key)
            result = type_cipher.caesar_decrypt(ciphertext, shift)
        elif method == "Root 13 Cipher":
            if key:
                flash("Root 13 Cipher tidak membutuhkan kunci. Kunci akan diabaikan.")
            result = type_cipher.root13_decrypt(ciphertext)
        elif method == "Vigenere Cipher":
            if not key.isalpha():
                flash("Kunci untuk Vigenere Cipher harus berupa huruf.")
                return redirect(url_for('decrypt'))
            result = type_cipher.vigenere_decrypt(ciphertext, key)
        elif method == "Beaufort Cipher":
            if not key.isalpha():
                flash("Kunci untuk Beaufort Cipher harus berupa huruf.")
                return redirect(url_for('decrypt'))
            result = type_cipher.beaufort_decrypt(ciphertext, key)
        elif method == "Autokey Cipher":
            if not key.isalpha():
                flash("Kunci untuk Autokey Cipher harus berupa huruf.")
                return redirect(url_for('decrypt'))
            result = type_cipher.autokey_decrypt(ciphertext, key)
        else:
            flash("Pilih metode dekripsi.")
            return redirect(url_for('decrypt'))

        return render_template('decrypt.html', result=result, method=method, input_text=ciphertext, key=key)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
