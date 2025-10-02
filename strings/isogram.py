def is_isogram(string):
    letters = [char.lower() for char in string if char.isalpha()]
    return len(letters) == len(set(letters))
