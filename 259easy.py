"""Challenge #259 [Easy] Clarence the Slow Typist

Full problem description at: https://redd.it/4bc3el"""
from math import sqrt

def coords(digit):
    """Find the coordinates of the given digit."""
    digits = "123456789.0"
    index = digits.index(digit)
    return (index % 3, index // 3)

def distance(start, end):
    """Find the distance between two different coordinates. Assume unit distance is 1"""
    x_diff = abs(end[0] - start[0])
    y_diff = abs(end[1] - start[1])
    return sqrt((x_diff ** 2) + (y_diff ** 2))

def measure(ip):
    """Given an ip address string, measure the distance travelled if pressing the digits in hunt-and-peck style."""
    prev_char = ip[0]
    total_distance = 0.0
    for char in ip[1:]:
        total_distance += distance(coords(prev_char), coords(char))
        prev_char = char
    print("Total distance for IP '{0}' was {1}cm".format(ip, total_distance))

if __name__ == "__main__":
    measure("219.45.143.143")
    measure("0.0.0.0")
    measure("127.0.0.1")
