def is_pangram(sentence):
    mask = 0

    for char in sentence:
        if char.isalpha():
            mask |= 1 << (ord(char.lower()) - ord("a"))

    return mask == (1 << 26) - 1
