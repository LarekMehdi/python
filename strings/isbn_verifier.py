def is_valid(isbn):

    allowed = set("0123456789-Xx")
    for char in isbn:
        if char not in allowed:
            return False
    
    nums = [c for c in isbn if c.isdigit() or c.upper() == 'X']
    
    if len(nums) != 10:
        return False

    total = 0
    for i, c in enumerate(nums, start=1):
        if c.upper() == 'X':
            if i != 10:
                return False
            val = 10
        else:
            val = int(c)
        total += i * val

    return total % 11 == 0
