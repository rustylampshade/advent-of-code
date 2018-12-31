import math
import re

def distance_from(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

class Nanobot(object):
    def __init__(self, input_string):
        match_groups = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', input_string).groups()
        self.pos = (int(match_groups[0]), int(match_groups[1]), int(match_groups[2]))
        self.radius = int(match_groups[3])

    def distance_from(self, point):
        return distance_from(self.pos, point)

    def intersects_cube(self, cube):
        dist = self.radius
        if self.pos[0] < cube.xmin or self.pos[0] > cube.xmax:
            if self.pos[0] < cube.xmin:
                dist -= (cube.xmin - self.pos[0])
            elif self.pos[0] > cube.xmax:
                dist -= (self.pos[0] - cube.xmax)
            if dist < 0:
                return False
        if self.pos[1] < cube.ymin or self.pos[1] > cube.ymin:
            if self.pos[1] < cube.ymin:
                dist -= (cube.ymin - self.pos[1])
            elif self.pos[1] > cube.ymax:
                dist -= (self.pos[1] - cube.ymax)
            if dist < 0:
                return False
        if self.pos[2] < cube.zmin or self.pos[2] > cube.zmax:
            if self.pos[2] < cube.zmin:
                dist -= (cube.zmin - self.pos[2])
            elif self.pos[2] > cube.zmax:
                dist -= (self.pos[2] - cube.zmax)
            if dist < 0:
                return False
        #print 'Think that {0} is within {1} of {2}'.format(vars(cube), dist, vars(self))
        return True

class Cube(object):
    def __init__(self, corner, size):
        self.xmin = corner[0]
        self.xmax = corner[0] + size - 1
        self.ymin = corner[1]
        self.ymax = corner[1] + size - 1
        self.zmin = corner[2]
        self.zmax = corner[2] + size - 1
        self.size = size
        self.corner = corner
    
    def get_quadrants(self):
        qsize = self.size / 2
        def shift(pos, delta):
            return (pos[0]+delta[0], pos[1]+delta[1], pos[2]+delta[2])
        return [Cube(qcorner, qsize) for qcorner in [
            self.corner, 
            shift(self.corner, (qsize,0,0)), 
            shift(self.corner, (0,qsize,0)), 
            shift(self.corner, (qsize,qsize,0)),
            shift(self.corner, (0,0,qsize)),
            shift(self.corner, (qsize,0,qsize)),
            shift(self.corner, (0,qsize,qsize)),
            shift(self.corner, (qsize,qsize,qsize))
        ]]
    
def find_densest_quadrants(cube):
    results = [(q, len([bot for bot in swarm if bot.intersects_cube(q)])) for q in cube.get_quadrants()]
    hottest_quadrant = max([r[1] for r in results])
    return [(r[0], r[1]) for r in results if r[1] == hottest_quadrant]


# Create all nanobots from the puzzle inputs
with open('inputs/23_1.txt', 'r') as aoc_input:
    swarm = [Nanobot(line) for line in aoc_input.read().rstrip('\n').split('\n')]

# Part 1: Find the bot with the largest radius, and see how many other bots are within range of it.
largest_radius_bot = sorted(swarm, key=lambda x: x.radius, reverse=True)[0]
print 'There are {0} total nanobots within {1} distance of the largest radius nanobot at {2}'.format(
    len([bot for bot in swarm if bot.distance_from(largest_radius_bot.pos) <= largest_radius_bot.radius]),
    largest_radius_bot.radius,
    largest_radius_bot.pos
)

# Part 2: Find the coordinate in 3-D space with the most bots in range.

# What is the relevant gridspace? Find the smallest cube that fits all nanobot's signal spheres.
min_point = (min(b.pos[0]-b.radius for b in swarm), min(b.pos[1]-b.radius for b in swarm), min(b.pos[2]-b.radius for b in swarm))
max_point = (max(b.pos[0]+b.radius for b in swarm), max(b.pos[1]+b.radius for b in swarm), max(b.pos[2]+b.radius for b in swarm))
largest_edge = max(max_point[0] - min_point[0], max_point[1] - min_point[1], max_point[2] - min_point[2])
gridspace = Cube(min_point, int(2**math.ceil(math.log(largest_edge, 2))))

# Definitionally, the starting gridspace cube sees all bots.
viable = {gridspace: len(swarm)}

# Do a BFS basically, halving the gridspace into 8 equally sized quadrant cubes to zero in on the best points.
for size_pow in range(int(math.ceil(math.log(gridspace.size, 2))), 0, -1):
    size = 2**size_pow
    current_round = {}
    for cube in viable:
        current_round.update({cube:density for cube, density in find_densest_quadrants(cube)})
    current_high_score = max(current_round.values())
    viable = {k:v for k, v in current_round.items() if v == current_high_score}
    print 'After round 2^{0}, there are {1} quadrants under consideration with {2} bots in range'.format(size_pow, len(viable), max(viable.values()))

closest = sorted([v.corner for v in viable.keys()], key=lambda x: distance_from((0,0,0), x))[0]
print 'The teleportation point is {0}, which is {1} distance away from origin.'.format(closest, distance_from((0,0,0), closest))