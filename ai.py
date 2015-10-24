import argparse
import json
import sys

boardstr = sys.argv[3]
boardstr = json.dumps(board)

color = sys.argv[5]
if color == 'black':
    color = 'b'
else color = 'w'

dim = 8

squares = boardstr['squares']
board = []
boardstart = 0
for i in range(dim):
    board[i] = squares[0:dim]
    boardstart = boardstart + dim


def is_valid(x, y):
    return

def solve():
    for i in board:
        for square in i:
            if  

    # return the move
    exit(move)


if __name == '__main__':
    solve()
