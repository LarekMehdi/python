"""Your task is to translate text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
Rule 1
If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

Rule 2
If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

Rule 3
If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

Rule 4
If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word."""

def translate(text):
    text = text.strip()
    if not text:
        return text
    if start_with_vowel(text) or start_rule_1(text):
        return text + 'ay'
    else:
        if has_qu(text):
            parts = split_after_qu(text)
            text = parts[1] + parts[0]
            return text + 'ay' 
        if has_y(text):
            parts = text.lower().split('y', 1)
            text = parts[1] + parts[0]
            return text + 'ay' 
        if has_vowel(text):
            idx = first_vowel_index(text)
            before = text[:idx]
            after = text[idx:]
            text = after + before
            return text + 'ay' 
        
        


def start_with_vowel(text):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    first_char = text[0]
    return first_char.lower() in VOWELS

def has_vowel(text):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    return any(c.lower() in VOWELS for c in text)

def start_rule_1(text):
    return text.startswith('xr') or text.startswith('yt')

def has_qu(text):
    return 'qu' in text.lower()

def split_after_qu(text):
    idx = text.find("qu")
    if idx != -1:
        return [text[:idx+2], text[idx+2:]]
    return [text]

def split_before_qu(text):
    idx = text.find("qu")
    if idx != -1:
        return text[:idx+2], text[idx+2:]
    return '', text

def has_y(text):
    return 'y' in text.lower()

def first_vowel_index(text):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(text)):
        if text[i].lower() in VOWELS:
            return i
    return -1


