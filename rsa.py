#!/usr/bin/python3
import sys


def facto(num):
    """ return 2 factors for a given number"""
    f1 = 2
    while (num % f1):
        if (f1 <= num):
            f1 += 1

    f2 = num // f1
    return (f2, f1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()


for line in lines:
    num = int(line.rstrip())
    f2, f1 = facto(num)
    print(f"{num}={f2}*{f1}")
