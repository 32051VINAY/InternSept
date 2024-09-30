import cv2
import numpy as np

def encrypt_image(image_path, encryption_key):
    """Encrypts an image using pixel manipulation.

    Args:
        image_path: Path to the image file.
        encryption_key: A numerical value used for encryption.

    Returns:
        The encrypted image as a NumPy array.
    """

    image = cv2.imread(image_path)
    encrypted_image = np.copy(image)

    # Perform pixel manipulation based on the encryption key
    for i in range(encrypted_image.shape[0]):
        for j in range(encrypted_image.shape[1]):
            for k in range(encrypted_image.shape[2]):
                encrypted_image[i, j, k] = (encrypted_image[i, j, k] + encryption_key) % 256

    return encrypted_image

def decrypt_image(encrypted_image, encryption_key):
    """Decrypts an encrypted image.

    Args:
        encrypted_image: The encrypted image as a NumPy array.
        encryption_key: The same encryption key used for encryption.

    Returns:
        The decrypted image as a NumPy array.
    """

    decrypted_image = np.copy(encrypted_image)

    # Reverse the pixel manipulation using the encryption key
    for i in range(decrypted_image.shape[0]):
        for j in range(decrypted_image.shape[1]):
            for k in range(decrypted_image.shape[2]):
                decrypted_image[i, j, k] = (decrypted_image[i, j, k] - encryption_key) % 256

    return decrypted_image

def save_image(image, filename):
    """Saves an image as a JPEG file.

    Args:
        image: The image as a NumPy array.
        filename: The desired filename for the saved image.
    """

    cv2.imwrite(filename, image)

if __name__ == "__main__":
    image_path = "your_image.jpg"
    encryption_key = 123  # Replace with your desired encryption key

    encrypted_image = encrypt_image(image_path, encryption_key)
    save_image(encrypted_image, "encrypted_image.jpg")

    decrypted_image = decrypt_image(encrypted_image, encryption_key)
    save_image(decrypted_image, "decrypted_image.jpg")