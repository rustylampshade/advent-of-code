
with open('inputs/6_1.txt', 'r') as aoc_input:
    points = [(int(p.split(',')[0]), int(p.split(',')[1])) for p in aoc_input.read().rstrip().split('\n')]

min_x = min([p[0] for p in points])
max_x = max([p[0] for p in points])
min_y = min([p[1] for p in points])
max_y = max([p[1] for p in points])

def manhattan_distance(pair, point):
    return abs(pair[0] - point[0]) + abs(pair[1] - point[1])

# PART 1

# Literally traverse the whole gridspace of a rectangle that barely fits the points (anything beyond this
# space is infinite plane that rules out an edge-point, and we can ignore). For every point on the grid, do
# full calculation against every Point and save a heatmap. 

# The fulltracker really is a fulltracker of doom since I know how close that coordinate is to ANYTHING.

# Then afterwards go count the coordinates that are closest to Point A, closest to Point B, etc.
# Exclude edge Points that have infinite domain.
# That's the answer! Bleh

fulltracker = {}
counter = {}
for point in points:
    counter[point] = 0
for i in range(min_x, max_x):
    if i not in fulltracker:
        fulltracker[i] = {} 
    for j in range(min_y, max_y):
        if j not in fulltracker[i]:
            fulltracker[i][j] = {}
        for point in points:
            fulltracker[i][j][point] = manhattan_distance((i, j), point)

        min_distance = min([distance for distance in fulltracker[i][j].values()])
        match = [(point, distance) for point, distance in fulltracker[i][j].items() if distance == min_distance]
        if len(match) == 1:
            counter[match[0][0]] += 1
        
# invalidate infinites
for point in points:
    if point[0] in [min_x, max_x] or point[1] in [min_y, max_y]:
        del counter[point]
print max(counter.values())


# PART 2
# Big Big Big gridspace, and impractical to do a slow Manhattan recalculation for every one. Instead, we're walking
# gridspace in a particular order. Like a typewriter, we seek from -x to +x for a given y, until we find one that's
# sub-ten-thousand. By moving only ONE coordinate, we can carefully remember the subtotal from the previous x value
# and adjust it: We're moving exactly one unit closer to some Points, and exactly one unit further from some other 
# set of Points. Careful indexing into a sorted list of Points lets us know how to adjust the subtotal. 
# When a good x value is found, add it to a list, and then continue seeking from x+1. 
# When you exhaust an entire row, bump to the next row (y+1) and repeat the whole process.
# Eventually we check the entire gridspace having calculated manhattans by hand for only 1 point per row.

# This ASSUMES that every point with sum(manhattan)<10k is the same region. The 'explore' function was going to be
# a crazy implementation that determined different regional blocks of close points, but maybe it's mathematically
# impossible to have two+ clusters of points in gridspace that meet the condition.

# This also seems to have WAY too large of bounds.

def advance_idx_until_match(idx, max_idx, subtotal, values, j, points):
    slice_point = 0
    max_slice = len(values)
    while subtotal > 10000 and idx <= max_idx:
        while slice_point < max_slice and values[slice_point] <= idx:
            slice_point += 1
        idx += 1
        subtotal -= (max_slice - slice_point)
        subtotal += slice_point
        """
        if subtotal != slow_manhattan(idx, j, points):
            print 'ALERT! WRONG LOGIC AT ({0},{1})'.format(idx, j)
            print 'Supposed: {0}'.format(subtotal)
            print 'Real: {0}'.format(slow_manhattan(idx,j,points))
            print 'Values: {0}'.format(values)
            print 'Slice_Point: {0}'.format(slice_point)
            print 'Nearby: {0}'.format(values[slice_point-3:slice_point+3])
            print 'Z: {0}'.format(values[slice_point])
            print 'Z: {0}'.format(values[slice_point] < idx)
            import sys
            sys.exit(1)
        """
    return idx, subtotal

def slow_manhattan(i, j, points):
    subtotal = 0
    for point in points:
        subtotal += abs(i - point[0]) + abs(j - point[1])
    return subtotal

def explore(coords):
    print '{0} has a good subtotal'.format(coords)

x = sorted([int(point[0]) for point in points])
y = sorted([int(point[1]) for point in points])
point_count = len(x)

i = min_x - 10000
j = min_y - 10000
matches = []
while j <= max_y + 10000:
    starting_sum = slow_manhattan(i, j, points)
    i_prime, subtotal = advance_idx_until_match(i, max_x + 10000, starting_sum, x, j, points)
    if subtotal < 10000:
        explore((i_prime, j))
        matches.append((i_prime, j))
        i = i_prime + 1
    else:
        # Ran out of x options, next row!
        i = min_x - 10000
        j += 1 

print matches
print len(matches)