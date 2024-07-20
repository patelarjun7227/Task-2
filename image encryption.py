from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open("C:\Users\ARJUN\Desktop\BUSINESS\_b1f05091-4180-444a-9a93-567d5ab6636f.jpg")
    # Convert the image to a NumPy array
    image_data = np.array(image)

    # Perform XOR operation on each pixel with the key
    encrypted_data = image_data ^ key

    # Convert the encrypted data back to an image
    encrypted_image = Image.fromarray(encrypted_data)

    # Save the encrypted image
    encrypted_image.save('encrypted_image.png')

    return 'encrypted_image.png'

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    # Convert the image to a NumPy array
    encrypted_data = np.array(encrypted_image)

    # Perform XOR operation on each pixel with the key to decrypt
    decrypted_data = encrypted_data ^ key

    # Convert the decrypted data back to an image
    decrypted_image = Image.fromarray(decrypted_data)

    # Save the decrypted image
    decrypted_image.save('decrypted_image.png')

    return 'decrypted_image.png'

def main():
    image_path = 'input_image.png'  # Path to the image you want to encrypt
    key = 123  # Key for encryption and decryption (use any integer)

    print("Encrypting the image...")
    encrypted_image_path = encrypt_image(image_path, key)
    print(f"Encrypted image saved as {encrypted_image_path}")

    print("Decrypting the image...")
    decrypted_image_path = decrypt_image(encrypted_image_path, key)
    print(f"Decrypted image saved as {decrypted_image_path}")

if __name__ == "__main__":
    main()
