#! /usr/bin/env python3

from functools import reduce
import operator

heightmap = []
with open('9.txt', 'r') as infile:
    for line in infile.readlines():
        heightmap.append([11] + [int(n) for n in list(line.strip())] + [11])
eleven_row = [11] * len(heightmap[0])
heightmap.insert(0, eleven_row)
heightmap.append(eleven_row)

lowpoints = []
for j, row in enumerate(heightmap[1:-1], start=1):
    for i, h in enumerate(row[1:-1], start=1):
        if h < heightmap[j][i+1] and h < heightmap[j][i-1] and h < heightmap[j+1][i] and h < heightmap[j-1][i]:
            lowpoints.append((i, j))

print('Part 1: %s' % sum([heightmap[j][i] + 1 for i, j in lowpoints]))

def basin_friends(i, j):
    for pt in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
        if heightmap[pt[1]][pt[0]] < 9 and pt not in basin:
            basin.append(pt)
            basin_friends(pt[0], pt[1])

basin_sizes = []
for low in lowpoints:
    basin = [low]
    basin_friends(low[0], low[1])
    basin_sizes.append(len(basin))

print('Part 2: %s' % reduce(operator.mul, sorted(basin_sizes)[-3:], 1))
