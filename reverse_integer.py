__author__ = 'lau'

# Reverse Integer


def reverse(x):
    is_negative = False
    if x < 0:
        is_negative = True
    num = str(abs(x))
    re = [x for x in num]
    re.reverse()
    result = int(''.join(re))
    if result > 2147483648:
            return 0
    else:
        if is_negative:
            return -result
        else:
            return result
