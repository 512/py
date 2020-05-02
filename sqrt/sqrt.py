#!/usr/bin/python

import sys


def next_digit(working, base):
    mult = 2 # for square roots
    for try_digit in range(9,-1,-1):
        #print("try digit %s" % digit)
        first = base*mult*10 + try_digit
        second = try_digit
        result = first*second
        if result <= working:
            return try_digit, result 

def root(n, size):
    answer = 0
    working = n
    while len(str(answer)) <= size:
        digit, result = next_digit(working, answer)
        answer = answer*10 + digit
        working = (working-result) * 100

    return answer


size = 50
n = None

args = sys.argv
if len(args) > 1:
    n = int(sys.argv[1])
if len(args) > 2:
    size = int(sys.argv[2])

if not n:
    n = int(input("square root of ?"))

print(n)
print()
raw = root(n, size)
print(raw)
