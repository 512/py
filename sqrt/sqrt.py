#!/usr/bin/python

"""
Calculates the square root of a number to N digits.

Reference: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

John L. Dalton
"""

import sys
import datetime

DECIMAL_POINT = '.'

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
        size = int(input("Number of digits: "))

    return n, size


def odd_length(lst):
    return 1 == len(lst) % 2

def ceil_div(a, b):
    # integer division with ceiling
    # ref: https://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
    return -(-a // b)

def group_into_pairs(n):
    """
    Given: n, the number to compute the square root of
    Return: a list of the digits of n, with decimal point, and leading or trailing zeroes, if needed.

    Add decimal point to end if missing.
    Separate the digits of n into pairs, starting from the decimal point and going left and right.
    Prepend or append with 0 if needed to ensure groups of two.
    Return list of ea

    Examples:
    5 -> 0 5 .
    15 -> 1 5 .
    153 -> 0 1 5 3 .
    3.145 -> 0 3 . 1 4 5 0
    """

    lst = [d for d in str(n)]
    if DECIMAL_POINT not in lst:
        lst.append(DECIMAL_POINT)
    p = lst.index(DECIMAL_POINT)
    before = lst[0:p]
    after = lst[p+1:]
    if odd_length(before):
        lst.insert(0, str(0))
    if odd_length(after):
        lst.append(str(0))
    return lst

def current_from_next_pair(lst, previous_remainder):
    """
    :param lst: the original number starting with the next pair to process
    if no pair, left, use 00

    :param previous_remainder: the remainder from the previous subtraction

    :return: a tuple containing ...
    -- the lst with the first pair of digits removed
    -- the current value to analyze

    Note: the first time, current will be the first pair itself, since
    the remainder is initialized to 0. i.e. sqrt(153) ==> current = 01 = 1
    """
    if not lst: # once lst is empty, keep bringing down 00
        addend = 0
    else:
        addend = int("%s%s" % (lst[0], lst[1]))
    current = previous_remainder * 100 + addend
    return lst[2:], current


def find_next_digit(current, partial):
    """
    Find p, y, and x as follows:

    Let c = current
    Let p = partial (the part of the root found so far, ignoring the decimal point)
    The first time through, p will be 0.
    Let y = x * (20p + x) ... Note: 20p + x is simply twice p with the digit x appended to the right

    Determine the greatest digit x such that x *(20p + x) <= c

    Try each digit from 9 to 0 until one works.
    Note: instead of brute force of starting with 9, we could take a short cut by starting with
    a value near c / (20p)

    :param current: the current value in the calculation (initially the value of the first pair of the original number)
    :param partial: the part of the root found so far, without decimal point (initially 0)
    :return: the digit x and the result of y (which should be subtracted from current)
    """

    MAX_DIGIT = 9
    MULTIPLIER = 20 # shift left in base ten, multiplied by 2 since doing square roots

    twenty_p = MULTIPLIER * partial
    upper_digit = MAX_DIGIT
    if twenty_p > 0:
        # short cut
        upper_digit = ceil_div(current, twenty_p + MAX_DIGIT)

    for x in range(upper_digit, -1, -1):
        y = x * (twenty_p + x)
        if y <= current:
            return x, y
    print("Unexpected state in find_next_digit")
    sys.exit(1)

def find_root(n, num_digits):
    answer_so_far = []
    partial_root = 0
    remainder = 0
    pairs = group_into_pairs(n)
    while len(answer_so_far) <= num_digits:

        # add decimal point to answer at correct spot
        if pairs and pairs[0] == DECIMAL_POINT:
            answer_so_far.append(DECIMAL_POINT)
            pairs = pairs[1:]
            continue

        pairs, current = current_from_next_pair(pairs, remainder)
        digit, result = find_next_digit(current, partial_root)
        answer_so_far.append(str(digit))

        partial_root = partial_root*10 + digit
        remainder = current - result
        if remainder == 0 and not pairs:
            # short circuit for rational answers
            break

    return partial_root, answer_so_far

def output(lst):
    print("".join(lst))

def output_with_breaks(lst, line_size=80):
    while lst:
        output(lst[:line_size])
        lst = lst[line_size:]

def main():
    n, size = get_input()
    print()
    print(f"Computing the square root of {n} to {size} digits")
    began = datetime.datetime.now().time()
    raw, digits  = find_root(n, size)
    ended = datetime.datetime.now().time()
    #print()
    #output(digits)
    print()
    output_with_breaks(digits)
    print()
    #print(f"check: root^2 = {raw*raw}")
    #print()
    print(f"Began at {began}")
    print(f"Ended at {ended}")


if __name__ == "__main__":
    main()
