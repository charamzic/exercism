def rotate(text, key):
    result = ""

    for char in text:
        if not char.isalpha():
            result += char
            continue

        if char.isupper():
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"

        old_position = alphabet.index(char)
        new_position = (old_position + key) % 26
        new_char = alphabet[new_position]

        result += new_char

    return result
