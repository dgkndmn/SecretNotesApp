# secret notes app'i yapılacak, görsel olsun, title, secret ve master key kısmı olsun.
# save encrypt ve decrypt butonları olsun. dosyayı kaydetsin.
from tkinter import *

import PIL.Image
from PIL import Image, ImageTk

window = Tk()
window.title("Secret Notes App")
window.minsize(width=350, height=570)
window.resizable(width=False,height=False)

image_path = "/Users/dogukan/Desktop/output-onlinepngtools.png"
new_width = 100
new_height = 100

def resize_image(image_path, new_width, new_height):
    img_pil = Image.open(image_path)
    img_resized = img_pil.resize((new_width, new_height), PIL.Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)
    return img_tk

resized_image = resize_image(image_path, new_width, new_height)
label = Label(image=resized_image)
label.pack(anchor="center")

label1 = Label(text="Enter the title")
label1.pack(anchor="center")

entry1 = Entry(width=20)
entry1.pack(anchor="center")
title = entry1.get()

label2 = Label(text="Enter your secret")
label2.pack(anchor="center")

text1 = Text(width=27,height=15)
text1.pack(anchor="center")
secret = text1.get("1.0",END)

label3 = Label(text="Enter a master key")
label3.pack(anchor="center")

entry2 = Entry(width=20)
entry2.pack(anchor="center")
password = entry2.get()




savebutton = Button(text="Save&Encrypt")
savebutton.pack(anchor="center")

decryptbutton = Button(text="Decrypt")
decryptbutton.pack(anchor="center")




window.mainloop()


