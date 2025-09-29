VOWELS = 'aeiou'

def translate_word(word):
    # 1
    if word[0] in VOWELS or word.startswith(("xr", "yt")):
        return word + "ay"
    # 2 
    for i in range(len(word)):
        if word[i:i+2] == "qu":
            return word[i+2:] + word[:i+2] + "ay"
        if word[i] in VOWELS or (word[i] == 'y' and i != 0): # 3
            return word[i:] + word[:i] + "ay"

    return word + "ay"

def translate(text):
    words = text.split()
    translated = [translate_word(word) for word in words]
    return " ".join(translated)
