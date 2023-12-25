#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = [ [ char for char in line.strip() ] for line in args.input.readlines() ]

gamma_strs = []
epsilon_strs = []

for i in range(len(lines[0])):
    ones = 0
    zeros = 0
    for line in lines:
        if line[i] == "0":
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        gamma_strs.append("1")
        epsilon_strs.append("0")
    else:
        gamma_strs.append("0")
        epsilon_strs.append("1")
print("Total:", int("".join(gamma_strs), base=2) * int("".join(epsilon_strs), base=2))
