#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Keep track of how many plays are still avilable to the user
    # and the choice selections
    move_selections = ['rock', 'paper', 'scissors']
    plays_available = []

    # Inner helper function that performs the recurrsion process
    # and checks the plays_available and adds them to an array
    def make_plays(moves, n):
        if n > 0:
            for i in range(len(move_selections)):
                make_plays(moves + [move_selections[i]], n-1)
        elif n == 0:
            return plays_available.append(moves)

    # returns the amount of moves available to the user
    # or creates a list within a list
    if n > 0:
        make_plays([], n)
        return plays_available
    elif n == 0:
        return [[]]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
