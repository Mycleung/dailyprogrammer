#!/usr/bin/env python
# DailyProgrammer 242 Intermediate: https://redd.it/3u6o56
# Usage: call 242intermediate.py <input-filename>

from optparse import OptionParser
from copy import deepcopy

parser = OptionParser()
opts, args = parser.parse_args()
input_file = args[0]

# showtimes is a dict of start_time: end_time
showtimes = {}
index = 0
with open(input_file, "r") as infile:
    for splitline in [line.strip().split(maxsplit=2) for line in infile]:
        print("Line: {}".format(splitline))
        if len(splitline) == 2:
            names_given = False
            # Only two elements, we haven't been given a show name, just name them by an index
            showtimes[index] = [int(x) for x in splitline[0:2]]
            index += 1
        elif len(splitline) == 3:
            # Three elements, we must have been given a name
            names_given = True
            showtimes[splitline[2]] = [int(x) for x in splitline[0:2]]

print("Input values were:")
for key, val in showtimes.items():
    print("Show: {}; Times: {}-{}".format(key, val[0], val[1]))

def choose(shows, time=0, watched=[], max=[]):
    """
    Brute force implementation:
        Starting from the time of the first show, recursively check every allowed path of watching/skipping the next
        show in the list until there are non left. Return the length of the largest returned "watched" list.

    :param shows: Shows we haven't watched yet
    :param time: Current time - determines which unwatched shows are yet to play
    :param watched: List containing the shows watched so far
    :return: Max number of shows it's possible to watch given the time and what we've watched so far.
    """
    for key, val in shows.items():
        if val[0] >= time:
            remaining = deepcopy(shows)
            del remaining[key]
            # What if we watched this one?
            pick = choose(remaining, val[1], watched + [key])
            # What if we didn't?
            leave = choose(remaining, val[0], watched)
            for longest in [pick, leave]:
                if len(longest)> len(max):
                    max = longest

    if len(watched) > len(max):
        return watched
    else:
        return max

max = choose(showtimes)

if names_given:
    print("It's possible to watch at most {} shows: {}".format(len(max), max))
else:
    print("It's possible to watch at most {} shows.".format(len(max)))