__author__ = 'lau'

# String to Integer

# I can converse Hex string into integer
# but I am a wrong answer x_x

def myAtoi(str_):
    is_negative = False
    if len(str_) == 0:
        return 0
    str_ = str_.strip()
    if str_.find('-') != -1 and str_.find('+') != -1:
        return 0
    else:
        str_ = str_.replace('+', '')
    if str_.count('-') == 1:
        is_negative = True
    str_ = str_.replace('-', '')
    numlist = []
    is_hex = False
    if str_.find('0x') != -1:
        is_hex = True
        str_ = str_.replace('0x', '')
    hex_dic = {
        'a': 10, 'b': 11, 'c': 12,
        'd': 13, 'e': 14, 'f': 15,
        '0': 0, '1': 1, '2': 2,
        '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8,
        '9': 9
    }
    for i in range(0, len(str_)):
        if str_[i] == 'a' or str_[i] == 'b' \
                or str_[i] == 'c' or str_[i] == 'd' \
                or str_[i] == 'e' or str_[i] == 'f':
            numlist.append(hex_dic.get(str_[i]))
            is_hex = True
        elif hex_dic.get(str_[i]) is not None:
            numlist.append(hex_dic.get(str_[i]))
        else:
            return 0
    result = 0
    if is_hex:
        for i in range(0, len(numlist)):
            result += numlist[i] * pow(16, len(numlist) - 1 - i)
    else:
        for i in range(0, len(numlist)):
            result += numlist[i] * pow(10, len(numlist) - 1 - i)
    if is_negative:
        if result > 2147483648:
            return -2147483648
        else:
            return -result
    else:
        if result > 2147483647:
            return 2147483647
        else:
            return result
