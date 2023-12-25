#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", type=argparse.FileType("r"))
args = parser.parse_args()

lines = [ line.strip() for line in args.input.readlines() ]

numbers = [ int(num) for num in lines[0].split(",") ]

boards = []

i = 2
while i < len(lines):
    board = [ [ (int(word), False) for word in line.split() ] for line in lines[i:i+5] ]
    boards.append(board)
    i += 6

def check_board(board, num):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i][0] == num:
                board[j][i] = (num, True)
                vertical = True
                for y in range(len(board)):
                    if not board[y][i][1]:
                        vertical = False
                        break
                if vertical:
                    return True
                for x in range(len(board[j])):
                    if not board[j][x][1]:
                        return False
                return True
    return False

finished = False
num_idx = 0
while num_idx < len(numbers) and not finished:
    num = numbers[num_idx]
    board_idx = 0
    while board_idx < len(boards) and not finished:
        board = boards[board_idx]
        if check_board(board, num):
            finished = True
        if not finished:
            board_idx += 1
    if not finished:
        num_idx += 1

total = 0
for y in range(len(board)):
    for x in range(len(board[y])):
        if not board[y][x][1]:
            total += board[y][x][0]
print("Result:", num * total)
