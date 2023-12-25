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
    boards.append((board, False))
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

last_num = None
last_finished = None
for num in numbers:
    board_idx = 0
    while board_idx < len(boards):
        if not boards[board_idx][1]:
            board = boards[board_idx][0]
            if check_board(board, num):
                last_num = num
                last_finished = board_idx
                boards[board_idx] = (board, True)
        board_idx += 1

board = boards[last_finished][0]
total = 0
for y in range(len(board)):
    for x in range(len(board[y])):
        if not board[y][x][1]:
            total += board[y][x][0]
print("Result:", last_num * total)
