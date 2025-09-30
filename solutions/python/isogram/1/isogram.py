def is_isogram(string):
    seen = []
    for char in string:
        if "A" <= char <= "Z":
            char = chr(ord(char) + 32)

        if char == " " or char == "-":
            continue

        for seen_char in seen:
            if char == seen_char:
                return False

        seen.append(char)

    return True
