#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", type=argparse.FileType("r"))
args = parser.parse_args()

line_re = re.compile("(\d+),(\d+)\s+->\s+(\d+),(\d+)")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __str__(self):
        return f"Line(front={self.front},back={self.back})"

    def __repr__(self):
        return self.__str__()

    def is_vertical(self):
        return self.front.x == self.back.x

    def is_horizontal(self):
        return self.front.y == self.back.y

lines = []
for matches in [ line_re.match(line) for line in args.input.readlines() ]:
    a, b = Point(int(matches[1]), int(matches[2])), Point(int(matches[3]), int(matches[4]))
    if a.x == b.x:
        if a.y <= b.y:
            lines.append(Line(a, b))
        else:
            lines.append(Line(b, a))
    elif a.y == b.y:
        if a.x <= b.x:
            lines.append(Line(a, b))
        else:
            lines.append(Line(b, a))

intersections = set()
for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        if i == j:
            continue
        a, b = lines[i], lines[j]
        if a.is_vertical() and b.is_horizontal():
            if b.front.x <= a.front.x and b.back.x >= a.front.x and a.front.y <= b.front.y and a.back.y >= b.front.y:
                intersections.add(Point(a.front.x, b.front.y))
        elif a.is_horizontal() and b.is_vertical():
            if a.front.x <= b.front.x and a.back.x >= b.front.x and b.front.y <= a.front.y and b.back.y >= a.front.y:
                intersections.add(Point(b.front.x, a.front.y))
        elif a.is_horizontal() and b.is_horizontal():
            if a.front.y == b.front.y and a.front.x <= b.back.x and a.back.x >= b.front.x:
                front = a.front.x if a.front.x >= b.front.x else b.front.x
                back = a.back.x if a.back.x <= b.back.x else b.back.x
                for x in range(front,back+1):
                    intersections.add(Point(x, a.front.y))
        elif a.is_vertical() and b.is_vertical():
            if a.front.x == b.front.x and a.front.y <= b.back.y and a.back.y >= b.front.y:
                front = a.front.y if a.front.y >= b.front.y else b.front.y
                back = a.back.y if a.back.y <= b.back.y else b.back.y
                for y in range(front,back+1):
                    intersections.add(Point(a.front.x, y))
print("Total:", len(intersections))
