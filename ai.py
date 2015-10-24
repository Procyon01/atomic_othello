#!/usr/bin/python
import argparse
import time
import json
import sys

'''
timelimit = sys.argv[7]
start_time = time.time()
'''

for i in sys.argv:
    print i

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
us = sys.argv[4]
them = ''
if us == 'black':
    us = u'b'
    them = u'w'
else: 
    us = u'w'
    them = u'b'

print us


# Valid list of moves
def solve():
    empties = [] 
    candidates = []
    for x in range(8):
        for y in range(8):
            if board[y][x] == '-':
                empties.append((y, x))
    
    for pos in empties:   # pos is an (x y) pair
        # if it's touching other piece
        for i in range(3):
            ny = pos[0] + i-1
            for j in range(3):
                nx = pos[1] + j-1

                # edge case (literally!)
                if nx < 0 or nx > 7:
                    continue
                if ny < 0 or ny > 7:
                    continue
                
                # if candidate is same as pos
                if (ny, nx) == pos:
                    continue

                # does it touch any pieces
                #print "is board[%d][%d] not %s?" % (nx, ny, board[nx][ny])
                if board[ny][nx] == u'w' or board[ny][nx] == u'b':
                    if (pos[0], pos[1]) not in candidates:
                        candidates.append( (pos[0], pos[1]) )

    for can in candidates:
        print(can)

    # check to see if we get points
    for pos in candidates:
      
        print '' 
        score = 0

        vy = pos[0]
        vx = pos[1]
        # horizontal left
        vx = vx - 1
        localscore = 0
        while vx > 0:
            if (board[vy][vx] == us):
                print "it's us"
                score = score + localscore
                print localscore
                break
            if (board[vy][vx] == them):
                print "it's them"
                localscore = localscore + 1
                vx = vx - 1
                continue
            else:   # it's blank
                print "it's blank"
                break
        
        vy = pos[0]
        vx = pos[1]
        # horizontal right
        vx = vx + 1
        localscore = 0
        while vx < 8:
            if (board[vy][vx] == us):
                print "it's us"
                score = score + localscore
                print localscore
                break
            if (board[vy][vx] == them):
                print "it's them"
                localscore = localscore + 1
                vx = vx + 1
                continue
            else:   # it's blank
                print "it's blank"
                break
        
        vy = pos[0]
        vx = pos[1]
        # vertical up
        vy = vy - 1
        localscore = 0
        while vy > 0:
            if (board[vy][vx] == us):
                print "it's us"
                score = score + localscore
                print localscore
                break
            if (board[vy][vx] == them):
                print "it's them"
                localscore = localscore + 1
                vy = vy - 1
                continue
            else:   # it's blank
                print "it's blank"
                break
        
        vy = pos[0]
        vx = pos[1]
        # vertical down
        vy = vy + 1
        localscore = 0
        while vy < 8:
            if (board[vy][vx] == us):
                print "it's us"
                score = score + localscore
                print localscore
                break
            if (board[vy][vx] == them):
                print "it's them"
                localscore = localscore + 1
                vy = vy + 1
                continue
            else:   # it's blank
                print "it's blank"
                break
        
        if (score > 0):
            valids.append( (pos[0], pos[1], score) )

    
    for move in valids:
        print(move)

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
