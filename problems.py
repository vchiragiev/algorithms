from typing import List
import math


def print_range_without_loop(n):
    if n > 0:
        print_range_without_loop(n-1)
        print(n)


def atoi(text, int_min, int_max):
    text_len = len(text)
    code_0 = ord('0')
    code_9 = ord('9')

    # handle zero text_len
    if text_len == 0: return None

    # handle sign
    negative = False
    if text[0] == '-':
        negative = True
        if text_len == 1: return None
        text = text[1:]
        text_len = text_len - 1

    # highest mask = 10^text_len-1 (10, 100, 1000, etc )
    mask = int(math.pow(10, text_len-1))
    res = 0.0
    for digit in text:
        code_d = ord(digit)
        if code_d < code_0 or code_d > code_9:
            return None
        res += (code_d - code_0) * mask
        mask = int(mask / 10)

    if negative:
        res *= -1
        if res < int_min:
            return None
    else:
        if res > int_max:
            return None
    return int(res)


if __name__ == "__main__":
    # print_range_without_loop(10)
    print(atoi("-32459",-100000, 100000))