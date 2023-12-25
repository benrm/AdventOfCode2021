#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

x, y = 0, 0
for line in args.input.readlines():
    words = line.strip().split()
    if words[0] == "forward":
        x += int(words[1])
    elif words[0] == "down":
        y += int(words[1])
    elif words[0] == "up":
        y -= int(words[1])
print("Result:", x * y)
