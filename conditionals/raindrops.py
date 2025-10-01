"""Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string."""

def convert(number):
    not_divisible = True
    result = ''
    if number % 3 == 0:
        result += 'Pling'
        not_divisible = False
    if number % 5 == 0:
        result += 'Plang'
        not_divisible = False
    if number % 7 == 0:
        result += 'Plong'
        not_divisible = False
    if not_divisible:
        return str(number)
    return result
    
