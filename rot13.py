# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ROT13, program code template


def encrypt(alphabet):
    REGULAR_CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    ENCRYPTED_CHARS = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if alphabet in REGULAR_CHARS:
        index = REGULAR_CHARS.index(alphabet)
        alphabet = ENCRYPTED_CHARS[index]
        return alphabet

    elif alphabet.lower() in REGULAR_CHARS:
        index = REGULAR_CHARS.index(alphabet.lower())
        alphabet = ENCRYPTED_CHARS[index]
        alphabet = alphabet.upper()
        return alphabet
    else:
        return alphabet


def row_encryption(sentence):
    encrypted_string = ""
    for char in sentence:
        encrypted_string += (encrypt(char))
    return encrypted_string


def main():
    print(row_encryption("hello, willy"))


main()