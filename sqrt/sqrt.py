#!/usr/bin/python

"""
Calculates the square root of a number to N digits.
John L. Dalton
"""

import sys

ZERO = '0'
POINT = '.'
MULTIPLIER = 2

def get_input():
    n = None
    size = None

    args = sys.argv
    if len(args) > 1:
        n = sys.argv[1]
    if len(args) > 2:
        size = int(sys.argv[2])

    if not n:
        n = input("Square root of ? ")
    if not size:
        size = int(input("Number of digits? "))

    return n, size

def odd_len(lst):
    return 1 == len(lst) % 2

def zeroize(n):
    """
    5 -> 05.
    15 -> 15.
    153 -> 0153.
    3.145 -> 03.1450
    """
    z = [x for x in str(n)]
    if POINT not in z:
        z.append(POINT)
    p = z.index(POINT)
    before = z[0:p]
    after = z[p+1:]
    if odd_len(before):
        z.insert(0, ZERO)
    if odd_len(after):
        z.append(ZERO)
    return z

def next_group(working, prev):
    if not working:
        addend = 0
    else:
        addend = int("%s%s" % (working[0], working[1]))
    current = prev * 100 + addend
    return current, working[2:]


def next_digit(current, ans_sofar):
    # brute force try each digit from 9 to 0 until correct one found
    for try_digit in range(9,-1,-1):
        first = ans_sofar * MULTIPLIER * 10 + try_digit
        second = try_digit
        result = first*second
        if result <= current:
            return try_digit, result 

def root(n, size):
    answer = 0
    chars = []
    working = 0
    base = zeroize(n)
    while len(chars) <= size:
        if base and base[0] == POINT:
            chars.append(POINT)
            base = base[1:]
            continue

        current, base = next_group(base, working)
        digit, result = next_digit(current, answer)
        chars.append(str(digit))

        answer = answer*10 + digit
        working = current - result
        if working == 0 and not base:
            break

    return answer, chars

if __name__ == "__main__":
    n, size = get_input()
    print("Computing the square root of %s to %s digits" % (n, size))
    print()
    raw, digits  = root(n, size)
    print("".join(digits))
