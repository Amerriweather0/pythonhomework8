
def get_shifts(date):
    # Keep only the digits from the date
    shifts = "".join(character for character in date
                     if character.isdigit())

    if not shifts:
        raise ValueError("Enter a date containing digits.")

    return [int(digit) for digit in shifts]


def encode(message, date):
    shifts = get_shifts(date)
    result = ""
    shift_index = 0

    for character in message:
        if character.isalpha() and character.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            base = ord("A") if character.isupper() else ord("a")
            shift = shifts[shift_index % len(shifts)]

            new_character = chr(
                (ord(character) - base + shift) % 26 + base
            )
            result += new_character
            shift_index += 1
        else:
            # Preserve spaces and punctuation
            result += character

    return result


def decode(message, date):
    shifts = get_shifts(date)
    result = ""
    shift_index = 0

    for character in message:
        if character.isalpha() and character.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            base = ord("A") if character.isupper() else ord("a")
            shift = shifts[shift_index % len(shifts)]

            new_character = chr(
                (ord(character) - base - shift) % 26 + base
            )
            result += new_character
            shift_index += 1
        else:
            result += character

    return result


def main():
    message = input("Enter a message to encode: ")
    date = input("Enter the agreed-upon date (e.g., 5/3/24): ")

    encrypted = encode(message, date)
    print("Encoded message:", encrypted)

    decrypted = decode(encrypted, date)
    print("Decoded message:", decrypted)


if __name__ == "__main__":
    main()
