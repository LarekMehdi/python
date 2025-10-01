def is_pangram(sentence):
    LETTERS = 'abcdefghiklmnopqrstuvwxyz'

    for letter in LETTERS:
        if letter not in sentence.lower():
            return False
    return True