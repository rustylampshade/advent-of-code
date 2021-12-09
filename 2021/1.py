#! /usr/bin/env python3

with open('1.txt', 'r') as infile:
    lines = list(map(int, map(str.strip, infile.readlines())))

def depth_increased(offset):
    counter = 0
    for i in range(0, len(lines) - offset):
        if lines[i] < lines[i+offset]:
            counter += 1
    return counter

print('Part 1: %s' % depth_increased(1))
print('Part 2: %s' % depth_increased(3))
