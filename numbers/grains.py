def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    dic = get_wheat_map(number)
    return dic[number]

def get_wheat_map(number):
    dic = dict()
    for i in range(1, number+1):
        if i > 1:
            last_num = dic[i-1]
            dic[i] = last_num * 2
        else:
            dic[i] = i

    return dic

def total():
    dic = get_wheat_map(64)
    result = 0
    for key, item in dic.items():
        result += item

    return result
