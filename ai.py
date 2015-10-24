#!/usr/bin/python
import argparse
import time
import json
import sys

'''
timelimit = sys.argv[7]
start_time = time.time()
'''

dim = 8

valids = []

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


# our color and opponent
us = sys.argv[5]
them = ''
if us == 'black':
    us = 'b'
    them = 'w'
else: 
    us = 'w'
    them = 'b'


# Valid list of moves
def solve():
    empties = [] 
    candidates = []
    for x in range(8):
        for y in range(8):
            if board[x][y] == '-':
                empties.add (x, y)
    
    for pos in empties:   # pos is an (x y) pair
        # if it's touching other piece
        for i in range(3):
            for j in range(3):
                candidatex = pos[0] + i
                candidatey = pos[1] + j

                # edge case (literally!)
                if candidatex == -1 or candidatex == 8:
                    continue
                if candidatey == -1 or candidatex == 8:
                    continue
                
                # if candidate is same as pos
                if (candidatex, cadidatey) == pos:
                    continue

                # does it touch any pieces
                if board[candidatex][candidatey] is not '-':
                    candidates.append( (candidatex, candidatey) )

    # check to see if we get points
    for pos in candidates:
        
        score = 0

        vx = pos[0]
        vy = pos[1]
        # horizontal left
        while vx > 0:
            localscore = 0
            vx = vx - 1
            if (board[vx][vy] is us):
                score = score + localscore
                break
            if (board[vx][vy] is them):
                score = score + localscore
                firstrun = False
                continue
            else:   # it's blank
                break
        
        vx = pos[0]
        vy = pos[1]
        # horizontal right
        while vx < 8:
            localscore = 0
            vx = vx + 1
            if (board[vx][vy] is us):
                score = score + localscore
                break
            if (board[vx][vy] is them):
                score = score + localscore
                firstrun = False
                continue
            else:   # it's blank
                break
        
        vx = pos[0]
        vy = pos[1]
        # vertical up
        while vy > 0:
            localscore = 0
            vy = vy - 1
            if (board[vx][vy] is us):
                score = score + localscore
                break
            if (board[vx][vy] is them):
                score = score + localscore
                firstrun = False
                continue
            else:   # it's blank
                break
        
        vx = pos[0]
        vy = pos[1]
        # vertical down
        while vy < 8:
            localscore = 0
            vy = vy - 1
            if (board[vx][vy] is us):
                score = score + localscore
                break
            if (board[vx][vy] is them):
                score = score + localscore
                firstrun = False
                continue
            else:   # it's blank
                break
        
        if (score > 0):
            valids.append( (pos[0], pos[1], score) )

    
    # make the best move
    best = 0
    bestmove = ()
    for move in valids:
        if (move[2] > best):
            bestmove = move

    # EXECUTE!!!!!!!!!!!!
    sys.exit(conv(bestmove[0], bestmove[1]) )


# For return codes
def conv(x, y):
    return (x * 8 + y) - 1

solve()
