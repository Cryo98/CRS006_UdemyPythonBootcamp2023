from Day_008_CaesarCipher_resources import LOGO, ALPHABET


def caesar_cipher(phrase, shift, direction):
    if direction == "encode":
        shift *= 1
    elif direction == "decode":
        shift *= -1
    ciphered_phrase = ""
    for letter in phrase:
        if letter in ALPHABET:
            idx = ALPHABET.index(letter)
            ciphered_phrase += ALPHABET[(idx+shift) % len(ALPHABET)]
        else:
            ciphered_phrase += letter
    print(f"The {direction}d phrase is: {ciphered_phrase}")


def main():
    print(LOGO)
    isRunning = True
    while isRunning:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        phrase = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        caesar_cipher(phrase=phrase, shift=shift, direction=direction)
        answer = input("Type 'yes' if you want to go again, otherwise type 'no': ").lower()
        isRunning = answer == 'yes'
    print("Goodbye.")


if __name__ == '__main__':
    main()
