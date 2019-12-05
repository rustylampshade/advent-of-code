
class Point(object):
    def __init__(self, line):
        self.starting_position = [int(num.strip()) for num in line.split('>')[0].split('<')[1].split(',')]
        self.current_position = self.starting_position
        self.velocity = [int(num.strip()) for num in line.split('<')[2].split('>')[0].split(',')]
    
    def advance_time(self):
        self.current_position[0] += self.velocity[0]
        self.current_position[1] += self.velocity[1]
    
    def reverse_time(self):
        self.current_position[0] -= self.velocity[0]
        self.current_position[1] -= self.velocity[1]

class Map(object):
    def __init__(self, points):
        self.points = points
        self.time = 0
    
    def draw(self):
        min_x = min([p.current_position[0] for p in self.points])
        max_x = max([p.current_position[0] for p in self.points])
        min_y = min([p.current_position[1] for p in self.points])
        max_y = max([p.current_position[1] for p in self.points])
        with open('outputs/drawing_{0}.txt'.format(self.time), 'w') as out:
            for j in range(min_y, max_y + 1):
                line = [' '] * (max_x - min_x + 1)
                for x in sorted([p.current_position[0] - min_x for p in self.points if p.current_position[1] == j]):
                    line[x] = '#'
                line_str = ''.join(line).rstrip()
                out.write(line_str + '\n')
    
    def animate(self):
        while True:
            x = [p.current_position[0] for p in self.points]
            old_width = max(x) - min(x)
            self.advance_time()
            new_x = [p.current_position[0] for p in self.points]
            new_width = max(new_x) - min(new_x)
            if new_width > old_width:
                self.reverse_time()
                self.draw()
                return
    
    def advance_time(self):
        self.time += 1
        [p.advance_time() for p in self.points]

    def reverse_time(self):
        self.time -= 1
        [p.reverse_time() for p in self.points]
        

with open('inputs/10_1.txt', 'r') as aoc_input:
    my_map = Map([Point(line) for line in aoc_input.read().rstrip('\n').split('\n')])

my_map.animate()