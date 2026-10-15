
def encipher(message, radius):
    # Remove spaces and convert to uppercase
    message = "".join(message.upper().split())

    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

    if len(message) % radius != 0:
        raise ValueError(
            "Message length must be divisible by the radius."
        )

    columns = len(message) // radius
    grid = [[""] * columns for _ in range(radius)]

    # Fill the grid down each column
    index = 0
    for col in range(columns):
        for row in range(radius):
            grid[row][col] = message[index]
            index += 1

    # Read across each row
    ciphertext = ""
    for row in range(radius):
        ciphertext += "".join(grid[row])

    return ciphertext


def decipher(ciphertext, radius):
    ciphertext = "".join(ciphertext.upper().split())

    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

    if len(ciphertext) % radius != 0:
        raise ValueError(
            "Ciphertext length must be divisible by the radius."
        )

    columns = len(ciphertext) // radius
    grid = [[""] * columns for _ in range(radius)]

    # Fill the grid across each row
    index = 0
    for row in range(radius):
        for col in range(columns):
            grid[row][col] = ciphertext[index]
            index += 1

    # Read down each column to restore the message
    message = ""
    for col in range(columns):
        for row in range(radius):
            message += grid[row][col]

    return message


def main():
    message = input("Enter a message without spaces: ")
    radius = int(input("Enter the radius (number of rows): "))

    encrypted = encipher(message, radius)
    print("Encrypted message:", encrypted)

    decrypted = decipher(encrypted, radius)
    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
