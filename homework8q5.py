
def locateLetter(board, letter):
    """Return the row and column of a letter."""
    letter = letter.upper()

    if letter == "Z":
        letter = "Y"

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == letter:
                return row, col

    raise ValueError(f"Letter {letter} is not in the checkerboard.")


def encrypt(message, board):
    """Convert a message into row-column pairs."""
    result = []

    for character in message.upper():
        if character.isalpha() and character.isascii():
            row, col = locateLetter(board, character)
            result.append(str(row) + str(col))

    return " ".join(result)


def decrypt(ciphertext, board):
    """Convert row-column pairs back into a message."""
    digits = "".join(ciphertext.split())

    if len(digits) % 2 != 0:
        raise ValueError("Ciphertext must contain pairs of digits.")

    result = ""

    for i in range(0, len(digits), 2):
        row = int(digits[i])
        col = int(digits[i + 1])

        if row < 0 or row >= len(board):
            raise ValueError("Invalid row number.")

        if col < 0 or col >= len(board[row]):
            raise ValueError("Invalid column number.")

        result += board[row][col]

    return result


def main():
    board = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"]
    ]

    message = input("Enter the message to encrypt: ")

    ciphertext = encrypt(message, board)
    plaintext = decrypt(ciphertext, board)

    print("Encrypted message:", ciphertext)
    print("Decrypted message:", plaintext)


if __name__ == "__main__":
    main()
