import re

class Nanobot(object):
    def __init__(self, input_string):
        match_groups = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', input_string).groups()
        self.pos = (int(match_groups[0]), int(match_groups[1]), int(match_groups[2]))
        self.radius = int(match_groups[3])

    def distance_from(self, point):
        return abs(self.pos[0] - point[0]) + abs(self.pos[1] - point[1]) + abs(self.pos[2] - point[2])

    def circle_center_in_box(self, box_corner, box_size):
        for dim in [0, 1, 2]:
            if self.pos[dim] not in xrange(box_corner[dim], box_corner[dim] + box_size):
                return False
        return True
    
    def box_edge_crosses_circle(self, box_corner, box_size):
        for edge in [0..8]:
            if overlaps:
                return True
        return False

    def intersects_box(self, box_corner, box_size):
        return self.circle_center_in_box(box_corner, box_size) or self.box_edge_crosses_circle(box_corner, box_size)

with open('inputs/23_1.txt', 'r') as aoc_input:
    swarm = [Nanobot(line) for line in aoc_input.read().rstrip('\n').split('\n')]

largest_radius_bot = sorted(swarm, key=lambda x: x.radius, reverse=True)[0]
print 'There are {0} total nanobots within {1} distance of the largest radius nanobot at {2}'.format(
    len([bot for bot in swarm if bot.distance_from(largest_radius_bot.pos) <= largest_radius_bot.radius]),
    largest_radius_bot.radius,
    largest_radius_bot.pos
)

def find_densest_quadrants(corner, size):
    size = size / 2
    results = []
    for quadrant in [corner,
                     (corner[0]+size, corner[1], corner[2]),
                     (corner[0], corner[1]+size, corner[2]),
                     (corner[0]+size, corner[1]+size, corner[2]),
                     (corner[0], corner[1], corner[2]+size),
                     (corner[0]+size, corner[1], corner[2]+size),
                     (corner[0], corner[1]+size, corner[2]+size),
                     (corner[0]+size, corner[1]+size, corner[2]+size)]:
        if size != 1:
            results.append((quadrant, len([bot for bot in swarm if bot.intersects_box(quadrant, size)])))
        else:
            results.append((quadrant, len([bot for bot in swarm if bot.distance_from(quadrant) <= bot.radius])))
    hottest_quadrant = max([r[1] for r in results])
    return [(r[0], hottest_quadrant) for r in results if r[1] == hottest_quadrant]

min_point = (min(b.pos[0]-b.radius for b in swarm), min(b.pos[1]-b.radius for b in swarm), min(b.pos[2]-b.radius for b in swarm))
max_point = (max(b.pos[0]+b.radius for b in swarm), max(b.pos[1]+b.radius for b in swarm), max(b.pos[2]+b.radius for b in swarm))
largest_edge = max(max_point[0] - min_point[0], max_point[1] - min_point[1], max_point[2] - min_point[2])
viable_corners = [min_point]

import math
for size_pow in range(int(math.ceil(math.log(largest_edge, 2))), 0, -1):
    size = 2**size_pow
    current_round_points = {}
    for corner in viable_corners:
        current_round_points.update({point:density for point, density in find_densest_quadrants(corner, size)})
    viable_corners = {k:v for k, v in current_round_points.items() if v == max(current_round_points.values())}
    print 'After round 2^{0}, there are {1} quadrants under consideration with {2} bots in range'.format(size_pow, len(viable_corners), max(viable_corners.values()))
print viable_corners