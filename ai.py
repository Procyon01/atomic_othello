#!/usr/bin/python
import argparse
import json
import sys

dim = 8

# json board
boardstr = sys.argv[3]
boardstr = json.dumps(board)

# python board
squares = boardstr['squares']
board = []
boardstart = 0
for i in range(dim):
    board[i] = squares[0:dim]
    boardstart = boardstart + dim

# our color
color = sys.argv[5]
if color == 'black':
    color = 'b'
else color = 'w'

"""


# Valid list of moves
def create_valids():
    empties = [] 
    for x in range(8):
        for y in range(8):
            if board[x][y] == '-':
                empties.add (x, y)
    
    for i in empties:
        
    


    # build horizontal and vertical lists
        horizontal = 

    # if it's touching other piece
    for i in board:
        for square in i:
            if 

    # if inline with other piece

"""

def solve():
    # return the move
    
    exit(20)


if __name == '__main__':
    solve()
