# -*- coding: utf-8 -*-
# Advent Challenge 5 - Counting Coins
# Write a script which, when given a positive integer, will tell you how many
# different ways there are, in British coinage, to make that amount in pence.
# e.g. python 05-CountingCoins.py 500 would return the number of different ways
# you can make 500p = £5 in standard British coinage.
from collections import defaultdict
from optparse import OptionParser

parser = OptionParser()
opts, args = parser.parse_args()

GOAL = int(args[0])
COINS = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


def choose(goal, coins):

    if goal == 0:
        # End goal
        return [defaultdict(int)]

    if (goal < 0) or (not coins):
        # No solutions
        return []

    # Take the first coin we can, either take some or don't
    # Either way we have a simpler problem we can solve recursively.
    coin = coins[0]
    take = choose(goal - coin, coins)
    for answer in take:
        answer[coin] += 1
    leave = choose(goal, coins[1:])

    return take + leave


def output_answer(answer_dict):
    output = []
    for coin, num in answer_dict.items():
        output.append("{}p: {}".format(coin, num))

    print(", ".join(output))

solns = choose(GOAL, COINS)
for soln in solns:
    output_answer(soln)

print("Number of solutions: {}".format(len(solns)))