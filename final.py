from tkinter import *
from tkinter import filedialog
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import struct

# Function to Encrypt Image
def encrypt(imagename, password):
    try:
        # Load image
        img = Image.open(imagename)
        width, height = img.size
        img_data = list(img.getdata())  # Image data

        # Convert the image data to bytes
        img_bytes = bytearray()
        for pixel in img_data:
            img_bytes.extend(pixel)
        
        # AES encryption setup
        password = password.ljust(16)  # Ensure the password is 16 bytes
        key = password.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv=os.urandom(16))  # Generate random IV
        
        # Pad the image data to be multiple of 16 bytes
        padded_data = pad(img_bytes, AES.block_size)
        
        # Encrypt the padded image data
        encrypted_data = cipher.encrypt(padded_data)
        
        # Save the encrypted image as a binary file
        enc_image_filename = imagename.split('.')[0] + '_enc.enc'
        with open(enc_image_filename, 'wb') as enc_file:
            # Write the IV, width, and height, then encrypted image data
            enc_file.write(cipher.iv)
            enc_file.write(struct.pack('I', width))  # Write width
            enc_file.write(struct.pack('I', height))  # Write height
            enc_file.write(encrypted_data)  # Write the encrypted image data
        
        print(f"Image encrypted successfully and saved as {enc_image_filename}")
        return enc_image_filename

    except Exception as e:
        print(f"Encryption failed: {e}")

# Function to Decrypt Image
def decrypt(enc_image, password):
    try:
        with open(enc_image, 'rb') as enc_file:
            iv = enc_file.read(16)  # Read the IV
            width = struct.unpack('I', enc_file.read(4))[0]  # Read width
            height = struct.unpack('I', enc_file.read(4))[0]  # Read height
            encrypted_data = enc_file.read()  # Read the encrypted data
        
        # AES decryption setup
        password = password.ljust(16)  # Ensure the password is 16 bytes
        key = password.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt the data and unpad it
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        
        # Rebuild the image from decrypted data
        img_data = [tuple(decrypted_data[i:i+3]) for i in range(0, len(decrypted_data), 3)]
        img = Image.new('RGB', (width, height))
        img.putdata(img_data)
        
        # Save the decrypted image
        dec_image_filename = enc_image.split('.')[0] + '_dec.png'
        img.save(dec_image_filename)
        print(f"Image decrypted successfully and saved as {dec_image_filename}")
    
    except Exception as e:
        print(f"Decryption failed: {e}")

# GUI for Image Encryption and Decryption
def encrypt_image():
    filename = filedialog.askopenfilename(title="Select an image file")
    if filename:
        password = password_entry.get()
        encrypt(filename, password)

def decrypt_image():
    filename = filedialog.askopenfilename(title="Select an encrypted file")
    if filename:
        password = password_entry.get()
        decrypt(filename, password)

# Setting up the GUI window
root = Tk()
root.title("Image Encryption and Decryption")
root.geometry("400x200")

# Password entry label and box
password_label = Label(root, text="Enter 16-byte password:")
password_label.pack(pady=10)
password_entry = Entry(root, width=25, show="*")
password_entry.pack(pady=5)

# Encrypt and Decrypt Buttons
encrypt_button = Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=5)
decrypt_button = Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=5)

root.mainloop()
