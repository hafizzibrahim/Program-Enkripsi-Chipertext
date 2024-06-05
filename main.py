import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import type_cipher

# Fungsi untuk membuka halaman enkripsi
def open_encrypt_page():
    main_frame.pack_forget()
    encrypt_decrypt_frame.pack()

    button_process.config(text="Enkripsi", command=encrypt)
    root.title("Enkripsi Teks")

# Fungsi untuk membuka halaman dekripsi
def open_decrypt_page():
    main_frame.pack_forget()
    encrypt_decrypt_frame.pack()

    button_process.config(text="Dekripsi", command=decrypt)
    root.title("Dekripsi Teks")

# Fungsi untuk kembali ke halaman utama dan menghapus input/output
def go_back():
    encrypt_decrypt_frame.pack_forget()
    main_frame.pack()
    root.title("Aplikasi Enkripsi dan Dekripsi Sederhana")
    
    # Menghapus input dan output
    entry_input.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    entry_result.delete(0, tk.END)
    combobox_method.set('')

# Fungsi untuk mengenkripsi berdasarkan metode yang dipilih
def encrypt():
    plaintext = entry_input.get().replace(" ", "")
    method = combobox_method.get()

    if method == "Caesar Cipher":
        shift = entry_key.get().replace(" ", "")
        if not shift.isdigit():
            messagebox.showerror("Error", "Kunci untuk Caesar Cipher harus berupa angka.")
            return
        shift = int(shift)
        result = type_cipher.caesar_encrypt(plaintext, shift)
    elif method == "Root 13 Cipher":
        if entry_key.get():
            messagebox.showwarning("Warning", "Root 13 Cipher tidak membutuhkan kunci. Kunci akan diabaikan.")
        result = type_cipher.root13_encrypt(plaintext)
    elif method == "Vigenere Cipher":
        key = entry_key.get().replace(" ", "")
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Vigenere Cipher harus berupa huruf.")
            return
        result = type_cipher.vigenere_encrypt(plaintext, key)
    elif method == "Beaufort Cipher":
        key = entry_key.get().replace(" ", "")
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Beaufort Cipher harus berupa huruf.")
            return
        result = type_cipher.beaufort_encrypt(plaintext, key)
    elif method == "Autokey Cipher":
        key = entry_key.get().replace(" ", "")
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Autokey Cipher harus berupa huruf.")
            return
        result = type_cipher.autokey_encrypt(plaintext, key)
    else:
        messagebox.showerror("Error", "Pilih metode enkripsi.")
        return

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

# Fungsi untuk mendekripsi berdasarkan metode yang dipilih
def decrypt():
    ciphertext = entry_input.get().replace(" ", "")
    method = combobox_method.get()

    if method == "Caesar Cipher":
        shift = entry_key.get().replace(" ", "")
        if not shift.isdigit():
            messagebox.showerror("Error", "Kunci untuk Caesar Cipher harus berupa angka.")
            return
        shift = int(shift)
        result = type_cipher.caesar_decrypt(ciphertext, shift)
    elif method == "Root 13 Cipher":
        if entry_key.get():
            messagebox.showwarning("Warning", "Root 13 Cipher tidak membutuhkan kunci. Kunci akan diabaikan.")
        result = type_cipher.root13_decrypt(ciphertext)
    elif method == "Vigenere Cipher":
        key = entry_key.get().replace(" ", "")
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Vigenere Cipher harus berupa huruf.")
            return
        result = type_cipher.vigenere_decrypt(ciphertext, key)
    elif method == "Beaufort Cipher":
        key = entry_key.get().replace(" ", "")
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Beaufort Cipher harus berupa huruf.")
            return
        result = type_cipher.beaufort_decrypt(ciphertext, key)
    elif method == "Autokey Cipher":
        key = entry_key.get().replace(" ", "")
        if not key.isalpha():
            messagebox.showerror("Error", "Kunci untuk Autokey Cipher harus berupa huruf.")
            return
        result = type_cipher.autokey_decrypt(ciphertext, key)
    else:
        messagebox.showerror("Error", "Pilih metode dekripsi.")
        return

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Aplikasi Enkripsi dan Dekripsi Sederhana")
root.geometry("500x500")
root.resizable(False, False)

# Frame utama untuk pilihan enkripsi/dekripsi
main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.pack(padx=20, pady=20, fill="x")

label_main = ttk.Label(main_frame, text="Pilih Mode:")
label_main.pack(pady=10)

button_encrypt_page = ttk.Button(main_frame, text="Enkripsi", command=open_encrypt_page)
button_encrypt_page.pack(pady=10)

button_decrypt_page = ttk.Button(main_frame, text="Dekripsi", command=open_decrypt_page)
button_decrypt_page.pack(pady=10)

# Frame untuk input dan hasil enkripsi/dekripsi
encrypt_decrypt_frame = ttk.Frame(root, padding=(20, 10))

# Frame untuk input teks
frame_input = ttk.LabelFrame(encrypt_decrypt_frame, text="Input Teks", padding=(20, 10))
frame_input.pack(padx=20, pady=10, fill="x")

label_input = ttk.Label(frame_input, text="Masukkan teks:")
label_input.pack(side="left")
entry_input = ttk.Entry(frame_input, width=50)
entry_input.pack(side="left", padx=10)

# Frame untuk memilih metode enkripsi/dekripsi
frame_method = ttk.LabelFrame(encrypt_decrypt_frame, text="Metode", padding=(20, 10))
frame_method.pack(padx=20, pady=10, fill="x")

label_method = ttk.Label(frame_method, text="Pilih metode:")
label_method.pack(side="left")
combobox_method = ttk.Combobox(frame_method, values=["Caesar Cipher", "Root 13 Cipher", "Vigenere Cipher", "Beaufort Cipher", "Autokey Cipher"], state="readonly")
combobox_method.pack(side="left", padx=10)

# Frame untuk input kunci
frame_key = ttk.LabelFrame(encrypt_decrypt_frame, text="Kunci", padding=(20, 10))
frame_key.pack(padx=20, pady=10, fill="x")

label_key = ttk.Label(frame_key, text="Masukkan kunci:")
label_key.pack(side="left")
entry_key = ttk.Entry(frame_key, width=50)
entry_key.pack(side="left", padx=10)

# Tombol untuk memproses (enkripsi/dekripsi)
frame_button = ttk.Frame(encrypt_decrypt_frame, padding=(20, 10))
frame_button.pack(padx=20, pady=10, fill="x")

button_process = ttk.Button(frame_button, text="Proses", command=None)  # Command akan diatur saat membuka halaman
button_process.pack()

# Tombol untuk kembali ke halaman utama
button_back = ttk.Button(frame_button, text="Kembali", command=go_back)
button_back.pack(pady=10)

# Frame untuk output teks hasil enkripsi/dekripsi
frame_result = ttk.LabelFrame(encrypt_decrypt_frame, text="Hasil", padding=(20, 10))
frame_result.pack(padx=20, pady=10, fill="x")

label_result = ttk.Label(frame_result, text="Hasil:")
label_result.pack(side="left")
entry_result = ttk.Entry(frame_result, width=50)
entry_result.pack(side="left", padx=10)

# Menjalankan aplikasi
root.mainloop()
