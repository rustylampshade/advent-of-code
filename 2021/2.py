#! /usr/bin/env python3

with open('2.txt', 'r') as infile:
    lines = [s.split(' ') for s in map(str.strip, infile.readlines())]

def submarine_swim():
    horizontal, vertical, aim = [0, 0, 0]
    for direction, val in lines:
        val = int(val)
        modifier = 1
        if direction == 'up':
            modifier = -1
        if direction in ['up', 'down']:
            aim += modifier * val
        else:
            horizontal += modifier * val
            vertical += aim * modifier * val
    return horizontal, vertical, aim

h, v, a = submarine_swim()
print('Part 1: %s' % (h * a))
print('Part 2: %s' % (h * v))
