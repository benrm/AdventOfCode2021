#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = [ int(line.strip()) for line in args.input.readlines() ]

total = 0
for i in range(3,len(lines)):
    if lines[i] > lines[i-3]:
        total += 1
print("Total:", total)
