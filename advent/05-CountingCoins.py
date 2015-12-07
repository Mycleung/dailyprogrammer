# -*- coding: utf-8 -*-
# Advent Challenge 5 - Counting Coins
# Write a script which, when given a positive integer, will tell you how many
# different ways there are, in British coinage, to make that amount in pence.
# e.g. python 05-CountingCoins.py 500 would return the number of different ways
# you can make 500p = £5 in standard British coinage.
from optparse import OptionParser

parser = OptionParser()
opts, args = parser.parse_args()

GOAL = int(args[0])
COINS = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
COUNT = 0


def permute(goal, coins):
    if goal == 0:
        # End goal, we've found a solution
        global COUNT
        COUNT += 1

    if (goal < 0) or (not coins):
        # No solutions
        return

    # Choose the first coin we can, either take some or don't
    # Either way we have a simpler problem we can solve recursively.
    permute(goal - coins[0], coins)

    # What if we don't?
    permute(goal, coins[1:])

permute(GOAL, COINS)

print("Number of solutions: {}".format(COUNT))