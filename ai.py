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
boardstr = sys.argv[2]
boardstr = json.loads(boardstr)


# python board
squares = boardstr['squares']
board = []
boardstart = 0
for i in range(dim):
    board.append(squares[boardstart:dim+boardstart])
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

print us
print them


# Valid list of moves
def solve():
    empties = [] 
    candidates = []
    for x in range(8):
        for y in range(8):
            if board[x][y] == '-':
                empties.append((x, y))
    
    for pos in empties:   # pos is an (x y) pair
        # if it's touching other piece
        for i in range(3):
            nx = pos[0] + i-1
            for j in range(3):
                ny = pos[1] + j-1

                # edge case (literally!)
                if nx < 0 or nx > 7:
                    continue
                if ny < 0 or ny > 7:
                    continue
                
                # if candidate is same as pos
                if (nx, ny) == pos:
                    continue

                # does it touch any pieces
                #print "is board[%d][%d] not %s?" % (nx, ny, board[nx][ny])
                if board[nx][ny] == u'w' or board[nx][ny] == u'b':
                    if (pos[0], pos[1]) not in candidates:
                        candidates.append( (pos[0], pos[1]) )

    for can in candidates:
        print(can)

    # check to see if we get points
    for pos in candidates:
       
        score = 0

        vx = pos[0]
        vy = pos[1]
        # horizontal left
        while vx > 0:
            localscore = 0
            if (board[vx][vy] == us):
                score = score + localscore
                print localscore
                break
            if (board[vx][vy] == them):
                localscore = localscore + 1
                vx = vx - 1
                continue
            else:   # it's blank
                break
        
        vx = pos[0]
        vy = pos[1]
        # horizontal right
        while vx < 8:
            localscore = 0
            if (board[vx][vy] == us):
                score = score + localscore
                print localscore
                break
            if (board[vx][vy] == them):
                localscore = localscore + 1
                vx = vx + 1
                continue
            else:   # it's blank
                break
        
        vx = pos[0]
        vy = pos[1]
        # vertical up
        while vy > 0:
            localscore = 0
            if (board[vx][vy] == us):
                score = score + localscore
                print localscore
                break
            if (board[vx][vy] == them):
                localscore = localscore + 1
                vy = vy - 1
                continue
            else:   # it's blank
                break
        
        vx = pos[0]
        vy = pos[1]
        # vertical down
        while vy < 8:
            localscore = 0
            if (board[vx][vy] == us):
                score = score + localscore
                print localscore
                break
            if (board[vx][vy] == them):
                localscore = localscore + 1
                vy = vy - 1
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
