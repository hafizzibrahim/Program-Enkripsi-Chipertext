import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Fungsi untuk Caesar Cipher
def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            ciphertext += char
    return ciphertext


# Fungsi untuk Vigenere Cipher
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


# Fungsi untuk mengenkripsi berdasarkan metode yang dipilih
def encrypt():
    plaintext = entry_plaintext.get()
    method = combobox_method.get()

    if method == "Caesar Cipher":
        shift = entry_key.get()
        if not shift.isdigit():
            messagebox.showerror("Error", "Kunci untuk Caesar Cipher harus berupa angka.")
            return
        shift = int(shift)
        ciphertext = caesar_encrypt(plaintext, shift)
    elif method == "Vigenere Cipher":
        key = entry_key.get()
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Vigenere Cipher harus berupa huruf.")
            return
        ciphertext = vigenere_encrypt(plaintext, key)
    else:
        messagebox.showerror("Error", "Pilih metode enkripsi.")
        return

    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, ciphertext)


# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Aplikasi Enkripsi Sederhana")
root.geometry("500x500")
root.resizable(False, False)

# Menambahkan gaya
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Frame untuk input plaintext
frame_plaintext = ttk.LabelFrame(root, text="Input Teks", padding=(20, 10))
frame_plaintext.pack(padx=20, pady=10, fill="x")

label_plaintext = ttk.Label(frame_plaintext, text="Masukkan teks:")
label_plaintext.pack(side="left")
entry_plaintext = ttk.Entry(frame_plaintext, width=50)
entry_plaintext.pack(side="left", padx=10)

# Frame untuk memilih metode enkripsi
frame_method = ttk.LabelFrame(root, text="Metode Enkripsi", padding=(20, 10))
frame_method.pack(padx=20, pady=10, fill="x")

label_method = ttk.Label(frame_method, text="Pilih metode:")
label_method.pack(side="left")
combobox_method = ttk.Combobox(frame_method, values=["Caesar Cipher", "Vigenere Cipher"], state="readonly")
combobox_method.pack(side="left", padx=10)

# Frame untuk input kunci
frame_key = ttk.LabelFrame(root, text="Kunci Enkripsi", padding=(20, 10))
frame_key.pack(padx=20, pady=10, fill="x")

label_key = ttk.Label(frame_key, text="Masukkan kunci:")
label_key.pack(side="left")
entry_key = ttk.Entry(frame_key, width=50)
entry_key.pack(side="left", padx=10)

# Tombol untuk mengenkripsi
frame_button = ttk.Frame(root, padding=(20, 10))
frame_button.pack(padx=20, pady=10, fill="x")

button_encrypt = ttk.Button(frame_button, text="Enkripsi", command=encrypt)
button_encrypt.pack()

# Frame untuk output ciphertext
frame_ciphertext = ttk.LabelFrame(root, text="Hasil Enkripsi", padding=(20, 10))
frame_ciphertext.pack(padx=20, pady=10, fill="x")

label_ciphertext = ttk.Label(frame_ciphertext, text="Hasil enkripsi:")
label_ciphertext.pack(side="left")
entry_ciphertext = ttk.Entry(frame_ciphertext, width=50)
entry_ciphertext.pack(side="left", padx=10)

# Menjalankan aplikasi
root.mainloop()
