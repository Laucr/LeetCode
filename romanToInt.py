__author__ = 'lau'

# Roman to Integer
# I（1） V（5） X（10） L（50） C（100） D（500） M（1000）


def romanToInt(s):
    roman_dict = {
        'I': 1, 'i': 1,
        'V': 5, 'v': 5,
        'X': 10, 'x': 10,
        'L': 50, 'l': 50,
        'C': 100, 'c': 100,
        'D': 500, 'd': 500,
        'M': 1000, 'm': 1000
    }
    s_list = list(s)
    n_list = []
    for i in range(0, len(s)):
        n_list.append(roman_dict.get(s_list[i]))
    result = 0
    for i in range(0, len(n_list) - 1):
        if n_list[i] < n_list[i+1]:
            result = -n_list[i] + result
        else:
            result += n_list[i]
    result += n_list[len(n_list) - 1]
    return result
