
def create_cipher_alphabet(keyword):
    keyword = keyword.upper()

    # Remove repeated letters from the keyword
    unique_keyword = ""
    for letter in keyword:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and letter not in unique_keyword:
            unique_keyword += letter

    # Add all remaining letters of the alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = unique_keyword

    for letter in alphabet:
        if letter not in cipher_alphabet:
            cipher_alphabet += letter

    return cipher_alphabet


def encode(message, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = create_cipher_alphabet(keyword)
    result = ""

    for character in message:
        if character.upper() in alphabet:
            index = alphabet.index(character.upper())
            new_character = cipher_alphabet[index]

            if character.islower():
                new_character = new_character.lower()

            result += new_character
        else:
            result += character

    return result


def decode(message, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = create_cipher_alphabet(keyword)
    result = ""

    for character in message:
        if character.upper() in cipher_alphabet:
            index = cipher_alphabet.index(character.upper())
            new_character = alphabet[index]

            if character.islower():
                new_character = new_character.lower()

            result += new_character
        else:
            result += character

    return result


def main():
    keyword = input("Enter a keyword: ")
    message = input("Enter a message to encode: ")

    encrypted = encode(message, keyword)
    print("Encoded message:", encrypted)

    decrypted = decode(encrypted, keyword)
    print("Decoded message:", decrypted)


if __name__ == "__main__":
    main()
