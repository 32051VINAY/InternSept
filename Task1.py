def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher Program")
    while True:
        mode = input("Choose mode (encrypt/decrypt) or 'exit' to quit: ").lower()

        if mode == 'exit':
            break

        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter shift value (positive or negative): "))

        if mode == 'encrypt':
            result = encrypt(message, shift)
            print("Encrypted Message:", result)
        elif mode == 'decrypt':
            result = decrypt(message, shift)
            print("Decrypted Message:", result)


if __name__ == "__main__":
    main()
