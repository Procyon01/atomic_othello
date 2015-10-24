import json
import sys

inputstr = sys.argv[1]
inputstr = json.dumps(board)

dim = 8

squares = inputstr['squares']
board = []
boardstart = 0
for i in range(dim):
    board[i] = squares[0:dim]
    boardstart = boardstart + dim


def is_valid():
    return

def solve():

    # return the move
    exit(move)


if __name == '__main__':
    solve()
