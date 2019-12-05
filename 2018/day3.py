import itertools

class Rectangle(object):
    def __init__(self, string_def):
        self.id = string_def.split(' ')[0]
        x, y = string_def.split(' ')[2].rstrip(':').split(',')
        self.xmin = int(x)
        self.ymin = int(y)
        width, height = string_def.split(' ')[3].split('x')
        self.xmax = int(x) + int(width)
        self.ymax = int(y) + int(height)
    
    def size(self):
        return (self.xmax - self.xmin) * (self.ymax - self.ymin)


with open('inputs/3_1.txt', 'r') as aoc_input:
    claims = [Rectangle(line) for line in aoc_input.read().rstrip('\n').split('\n')]

def overlap(r1, r2, conflicts):
    # If max-of-mins < min-of-maxes on both axis, they overlap.
    x_max_of_mins = max(r1.xmin, r2.xmin)
    y_max_of_mins = max(r1.ymin, r2.ymin)
    x_min_of_maxs = min(r1.xmax, r2.xmax)
    y_min_of_maxs = min(r1.ymax, r2.ymax)

    if x_max_of_mins >= x_min_of_maxs or y_max_of_mins >= y_min_of_maxs:
        return
    for i in range(x_max_of_mins, x_min_of_maxs):
        if i not in conflicts.keys():
            conflicts[i] = []
        for j in range(y_max_of_mins, y_min_of_maxs):
            if j not in conflicts[i]:
                conflicts[i].append(j)                
    return

conflicts = {}
for r1, r2 in itertools.combinations(claims, 2):
    overlap(r1, r2, conflicts) 
print sum([len(v) for v in conflicts.values()])

def contains_conflict(r, conflicts):
    for i in range(r.xmin, r.xmax):
        for j in range(r.ymin, r.ymax):
            if i in conflicts and j in conflicts[i]:
                return True
    return False

for c in claims:
    if not contains_conflict(c, conflicts):
        print 'Found it!! {0}'.format(c.id)