__author__ = 'lau'

# String to Integer


def myAtoi(str_):
    is_negative = False
    if len(str_) == 0:
        return 0
    str_ = str_.strip()
    if (str_.find('-') != -1 and str_.find('+') != -1) or str_.count('+') > 1 or str_.count('-') > 1:
        return 0
    else:
        str_ = str_.replace('+', '')
    if str_.count('-') == 1:
        is_negative = True
    str_ = str_.replace('-', '')
    numlist = []
    num_dic = {
        '0': 0, '1': 1, '2': 2,
        '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8,
        '9': 9
    }
    for i in range(0, len(str_)):
        if num_dic.get(str_[i]) is not None:
            numlist.append(num_dic.get(str_[i]))
        else:
            break
    result = 0
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
