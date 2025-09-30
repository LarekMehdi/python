# Newton-Raphson

def square_root(number):
    epsilon = 1e-10
    result = number / 2

    while abs((result * result) - number) > epsilon:
        result = (result + (number / result)) / 2

    return int(result)
