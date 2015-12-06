#!/usr/bin/env python
# DailyProgrammer 242 Intermediate: https://redd.it/3u6o56
# Usage: call 242intermediate.py <input-filename>

from optparse import OptionParser

parser = OptionParser()
opts, args = parser.parse_args()
input_file = args[0]

# showtimes is a dict of start_time: end_time
showtimes = {}
with open(input_file, "r") as infile:
    for start, end in [line.split() for line in infile.readlines()]:
        showtimes[int(start)] = int(end)

print("Input values were:")
for key, val in showtimes.items():
    print("{}: {}".format(key, val))
