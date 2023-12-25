#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

x, y, aim = 0, 0, 0
for line in args.input.readlines():
    words = line.strip().split()
    if words[0] == "forward":
        x += int(words[1])
        y += aim * int(words[1])
    elif words[0] == "down":
        aim += int(words[1])
    elif words[0] == "up":
        aim -= int(words[1])
print("Result:", x * y)
