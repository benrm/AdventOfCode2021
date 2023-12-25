#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = [ line.strip() for line in args.input.readlines() ]
length = len(lines[0])

product = 1
for compare in [ lambda ones, zeros : ones >= zeros, lambda ones, zeros : ones < zeros ]:
    working = { line for line in lines }
    i = 0
    while i < length and len(working) > 1:
        ones = 0
        zeros = 0
        for line in working:
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1
        future = working.copy()
        if compare(ones, zeros):
            for string in working:
                if string[i] == "0":
                    future.remove(string)
        else:
            for string in working:
                if string[i] == "1":
                    future.remove(string)
        working = future
        i += 1
    if len(working) > 1:
        raise Exception("working set has more than one entry")
    for string in working:
        product *= int(string, base=2)
print("Product:", product)
