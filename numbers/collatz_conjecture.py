def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    result = 0
    n = number
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            result += 1
        else:
            n = (int(n * 3) + 1)
            result += 1

    return result