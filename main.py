from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
import os

window = Tk()
window.title("Secret Notes App")
window.minsize(width=350, height=570)
window.resizable(width=False, height=False)

image_path = "/Users/dogukan/Desktop/output-onlinepngtools.png"
new_width = 100
new_height = 100

def resize_image(image_path, new_width, new_height):
    img_pil = Image.open(image_path)
    img_resized = img_pil.resize((new_width, new_height), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)
    return img_tk

resized_image = resize_image(image_path, new_width, new_height)
label = Label(image=resized_image)
label.pack(anchor="center")

label1 = Label(text="Enter the title")
label1.pack(anchor="center")

entry1 = Entry(width=20)
entry1.pack(anchor="center")

label2 = Label(text="Enter your secret")
label2.pack(anchor="center")

text1 = Text(width=27, height=15)
text1.pack(anchor="center")

label3 = Label(text="Enter a master key")
label3.pack(anchor="center")

entry2 = Entry(width=20)
entry2.pack(anchor="center")

def derive_key(master_key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )
    return base64.urlsafe_b64encode(kdf.derive(master_key.encode()))

def encrypt(secret, derived_key):
    cipher_suite = Fernet(derived_key)
    return cipher_suite.encrypt(secret.encode())

def decrypt(encrypted_data, derived_key):
    cipher_suite = Fernet(derived_key)
    original_text = cipher_suite.decrypt(encrypted_data).decode()
    return original_text


def save_encrypt():
    title = entry1.get()
    secret = text1.get("1.0", END)
    password = entry2.get()

    salt = os.urandom(16)

    derived_key = derive_key(password, salt)

    sifreli_metin = encrypt(secret, derived_key)

    if sifreli_metin is not None:
        filename = f"{title}.txt"
        with open(filename, "wb") as dosya:
            dosya.write(salt + sifreli_metin)


        entry1.delete(0, END)
        text1.delete("1.0", END)
        entry2.delete(0, END)

        messagebox.showinfo("Success", f"The secret is encrypted and saved as {filename}")


def decrypt_secret():
    title = entry1.get()
    password = entry2.get()

    try:
        with open(f"{title}.txt", "rb") as dosya:
            data = dosya.read()
            salt = data[:16]
            encrypted_data = data[16:]
            derived_key = derive_key(password, salt)
            original_text = decrypt(encrypted_data, derived_key)
            text1.delete("1.0", END)
            text1.insert("1.0", original_text)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Make sure the file exists.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

savebutton = Button(text="Save&Encrypt", command=save_encrypt)
savebutton.pack(anchor="center")

decryptbutton = Button(text="Decrypt", command=decrypt_secret)
decryptbutton.pack(anchor="center")

window.mainloop()
