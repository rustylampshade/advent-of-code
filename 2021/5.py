#! /usr/bin/env python3

with open('5.txt', 'r') as infile:
    lines = [s.split() for s in map(str.strip, infile.readlines())]

def visit(x, y):
    key = "{0},{1}".format(x, y)
    if key in heatmap:
        heatmap[key] += 1
    else:
        heatmap[key] = 1

def process_lines(include_diagonals=False):
    for segment in lines:
        x1, y1 = [int(n) for n in segment[0].split(',')]
        x2, y2 = [int(n) for n in segment[2].split(',')]
        
        if x1 != x2 and y1 == y2:
            direction = 1 if x2 > x1 else -1
            for i in range(x1, x2 + direction, direction):
                visit(i, y1)

        if x1 == x2 and y1 != y2:
            direction = 1 if y2 > y1 else -1
            for j in range(y1, y2 + direction, direction):
                visit(x1, j)

        if x1 != x2 and y1 != y2 and include_diagonals:
            xdirection = 1 if x2 > x1 else -1
            ydirection = 1 if y2 > y1 else -1
            j = y1
            for i in range(x1, x2 + xdirection, xdirection):
                visit(i, j)
                j += ydirection

heatmap = {}
process_lines()
print('Part 1: %s' % len({key for key, value in heatmap.items() if value >= 2}) )

heatmap = {}
process_lines(include_diagonals=True)
print('Part 2: %s' % len({key for key, value in heatmap.items() if value >= 2}) )
