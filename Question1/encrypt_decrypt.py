def encrypt(n, m, text):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + n + m) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') + n + m) % 26) + ord('A'))
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text

def decrypt(n, m, encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') - n - m) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') - n - m) % 26) + ord('A'))
        else:
            shifted_char = char
        decrypted_text += shifted_char
    return decrypted_text

def check_decryption(original_text, decrypted_text):
    if original_text == decrypted_text:
        print("Decryption successful! The decrypted text matches the original.")
        return True
    else:
        print("Decryption failed! The decrypted text does NOT match the original.")
        return False

if __name__ == "__main__":
    try:
        with open("raw_text.txt", "r") as file:
            raw_content = file.read()
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found. Please create this file with your text.")
        exit()

    while True:
        try:
            n = int(input("Enter the integer value for 'n': "))
            m = int(input("Enter the integer value for 'm': "))
            break
        except ValueError:
            print("Invalid input. Please enter integers for 'n' and 'm'.")

    encrypted_content = encrypt(n, m, raw_content)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_content)

    print("Encryption complete. The encrypted text has been written to 'encrypted_text.txt'.")

    decrypted_content = decrypt(n, m, encrypted_content)
    check_decryption(raw_content, decrypted_content)

    print("\nDecrypted text:")
    print(decrypted_content)