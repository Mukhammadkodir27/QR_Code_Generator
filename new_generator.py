from tkinter import *
from PIL import Image, ImageTk
import pyqrcode

root = Tk()
root.title("QR Code Generator")
root.geometry("500x700")  # Adjusted window size

# Load and set the background image
bg_image = Image.open("background3.jpg")  # Ensure the image path is correct
bg_image = bg_image.resize((500, 700), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Declare image_label globally
image_label = None


def generate():
    global image_label  # Correct global declaration
    link_name = name_entry.get().strip()
    link = link_entry.get().strip()
    if link_name and link:
        file_name = f"{link_name}.png"
        url = pyqrcode.create(link)
        url.png(file_name, scale=8)

        # Load and resize the QR code image
        qr_image = Image.open(file_name)
        qr_image = qr_image.resize(
            (350, 350), Image.ANTIALIAS)  # Adjusted size
        photo = ImageTk.PhotoImage(qr_image)

        # Update the image in the existing label or create a new label if one does not exist
        if image_label is None:
            image_label = Label(root, image=photo)
            image_label.place(x=75, y=350)  # Adjusted placement
        else:
            image_label.config(image=photo)

        image_label.image = photo  # Keep a reference to avoid garbage collection


# Widgets on top of the background
Label(root, text="QR Code Generator", fg="blue",
      font=("Arial", 24), bg="white").pack(pady=20)

Label(root, text="Link name", font=("Arial", 14), bg="white").pack()
name_entry = Entry(root, font=("Arial", 14), width=30)
name_entry.pack(pady=10)

Label(root, text="Link URL", font=("Arial", 14), bg="white").pack()
link_entry = Entry(root, font=("Arial", 14), width=30)
link_entry.pack(pady=10)

Button(root, text="Generate QR Code", font=(
    "Arial", 14), command=generate).pack(pady=20)

# Title or text at the bottom
Label(root, text="Created by Mukhammadkodir", font=("Arial", 14),
      fg="white", bg="black").pack(side=BOTTOM, fill=X)

root.mainloop()
