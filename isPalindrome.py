__author__ = 'lau'

# Palindrome Number


def isPalindrome(x):
    sq = 1
    t = x
    if x < 0:
        return False
    if x < -2147483648 or x > 2147483647:
        return False
    if 0 <= x <= 9:
        return True
    while t / 10 > 0:
        sq *= 10
        t = int(t / 10)
    sq = int(sq / 10)      # python2.7 do not need this.
    while x:
        low = x - int(x / 10) * 10
        high = int(x / sq)
        x = int((x - sq*high) / 10)
        sq = int(sq / 100)
        if low != high:
            return False
    return True
