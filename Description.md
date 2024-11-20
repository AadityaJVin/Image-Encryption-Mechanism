  Image Encryption and Decryption using AES Algorithm  
This project implements a robust and user-friendly system for encrypting and decrypting images using the   Advanced Encryption Standard (AES)  in   Cipher Block Chaining (CBC)   mode. Designed to protect sensitive image data, the system ensures confidentiality by allowing only authorized users with the correct password to access the original image. 
The project includes a graphical user interface (GUI) developed with Tkinter, providing an intuitive platform for image encryption and decryption tasks. It supports multiple image formats, such as PNG, JPEG, and BMP, and ensures secure encryption using a 16-byte password for key generation.
     **Features**  
-   AES Encryption in CBC Mode: Uses the AES algorithm in CBC mode for secure and efficient encryption.
-   Password-Based Encryption: Allows users to define a password, which is converted into a secure 16-byte encryption key.
-   GUI Interface: Provides a simple Tkinter-based graphical interface for easy interaction.
-   Multi-Format Support: Compatible with commonly used image formats, including PNG, JPEG, and BMP.
-   Padding for Security: Ensures encrypted data is padded to a 16-byte boundary, as required by AES in CBC mode.
-   Real-Time Operations: Encrypts and decrypts images in real-time with immediate feedback to the user.

**Technologies Used**  
-   Python 3.x: Core programming language for the project.
-   PyCryptodome: Used for AES encryption and decryption operations.
-   Pillow (PIL): For handling image processing tasks such as loading, converting, and saving images.
-   Tkinter: For creating the user-friendly GUI.

**How It Works**  
1.   Encryption: 
   - The user selects an image and provides a password.
   - The image is converted into raw byte data.
   - The AES algorithm encrypts the byte data using a key derived from the user’s password.
   - The encrypted data is saved as a new image with the same dimensions and format as the original.

2.   Decryption: 
   - The user selects an encrypted image and enters the same password used during encryption.
   - The AES algorithm decrypts the image data, restoring the original image.

 **Installation**  

1.   Clone the Repository  :
   git clone <--Link to this repository-->
   cd image-encryption-aes

2.   Set Up the Environment:
   - Install Python 3.x if not already installed.
   - Create a virtual environment (optional but recommended):
     
'''

     python3 -m venv myenv
     source myenv/bin/activate

3.   Install Required Libraries:
   
   pip install -r requirements.txt
   
5.   Run the Program:
   
   python final.py

Usage  
1. Launch the application by running `final.py`.
2. Use the GUI to:
   - Select an image file for encryption.
   - Enter a password to encrypt the image.
   - Save the encrypted image file.
   - Select an encrypted image file for decryption.
   - Enter the same password to decrypt the image and view the original  
     Future Scope  
- Adding support for additional image formats.
- Integrating cloud-based storage for encrypted images.
- Enhancing security with hybrid encryption methods.
- Optimizing performance for larger images.

Contributing  
Contributions are welcome! Feel free to fork the repository and submit a pull request with your changes or improvements.
