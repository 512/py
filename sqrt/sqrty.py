#!/usr/bin/python

"""
Calculates the square root of a number to N digits.
Using yield.

Reference: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

John L. Dalton
"""

import sys
import datetime

DECIMAL_POINT = '.'

def odd_length(lst):
    return 1 == len(lst) % 2

def ceil_div(a, b):
    # integer division with ceiling
    # ref: https://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
    return -(a // -b)

class RootCalculator:
    def __init__(self):
        self.pairs = []
        self.partial_root = 0
        self.remainder = 0
        self.result = 0

    def group_into_pairs(self,n):
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

    def current_from_next_pair(self):
        """
        Note: the first time, current will be the first pair itself, since
        the remainder is initialized to 0. i.e. sqrt(153) ==> current = 01 = 1
        """
        if not self.pairs: # once lst is empty, keep bringing down 00
            addend = 0
        else:
            addend = int("%s%s" % (self.pairs[0], self.pairs[1]))
        self.pairs = self.pairs[2:]
        return self.remainder * 100 + addend


    def find_next_digit(self):
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
        """

        MAX_DIGIT = 9
        MULTIPLIER = 20 # shift left in base ten, multiplied by 2 since doing square roots

        # add decimal point to answer at correct spot
        if self.pairs and self.pairs[0] == DECIMAL_POINT:
            self.pairs = self.pairs[1:]
            return DECIMAL_POINT

        if self.remainder == 0 and not self.pairs:
            # short circuit for rational answers
            return -1

        self.current = self.current_from_next_pair()

        twenty_p = MULTIPLIER * self.partial_root
        upper_digit = MAX_DIGIT
        if twenty_p > 0:
            # short cut
            upper_digit = ceil_div(self.current, twenty_p + MAX_DIGIT)

        for x in range(upper_digit, -1, -1):
            y = x * (twenty_p + x)
            if y <= self.current:
                self.remainder = self.current - y
                self.partial_root = self.partial_root*10 + x
                return x

        print("Unexpected state in find_next_digit")
        sys.exit(1)

    def sqrt(self, n):
        self.pairs = self.group_into_pairs(n)
        while True:
            yield self.find_next_digit()


def get_input():
    n = None
    size = None
    raw = None

    args = sys.argv
    if len(args) > 1:
        n = sys.argv[1]
    if len(args) > 2:
        size = int(sys.argv[2])
    if len(args) > 3:
        raw = sys.argv[3]

    if not n:
        n = input("Square root of ? ")
    if not size:
        size = int(input("Number of digits: "))

    return n, size, raw


def output(lst):
    print("".join(lst))


def output_with_breaks(lst, line_size=80):
    while lst:
        output(lst[:line_size])
        lst = lst[line_size:]

def show_answer(digits, size, raw):
    count = 0
    line_count = 0
    progress = None
    for d in digits:
        if d == -1:
            print(0)
            break
        print(d, end="")
        count += 1
        if not raw:
            line_count += 1
            if count % (size // 10) == 0:
                progress = f"    {100*(count / size)}% {datetime.datetime.now().time()}"
            if line_count == 80:
                line_count = 0
                if progress:
                    print(progress)
                    progress = None
                else:
                    print()
        if count == size:
            break

    print()
    print()

def main():
    n, size, raw = get_input()
    print()
    print(f"Computing the square root of {n} to {size} digits")
    print()

    began = datetime.datetime.now().time()

    digits = RootCalculator().sqrt(n)
    show_answer(digits, size, raw)

    ended = datetime.datetime.now().time()
    print(f"Began at {began}")
    print(f"Ended at {ended}")

if __name__ == "__main__":
    main()
