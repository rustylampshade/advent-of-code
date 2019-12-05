#! /usr/bin/env python

DIRECTIONS = {
    '>': (1, 0),
    '^': (0, -1),
    '<': (-1, 0),
    'v': (0, 1)
}

class Track(object):
    def __init__(self, lines):
        self.map = []
        self.carts = []
        self.time = 0
        starting_cart_name = 1
        for line_number, line_contents in enumerate(lines, 0):
            new_carts, scrubbed_line, starting_cart_name = self.extract_carts(line_contents, line_number, starting_cart_name)
            self.carts.extend(new_carts)
            self.map.append(list(scrubbed_line))

    def extract_carts(self, map_line, line_number, cart_name):
        carts = []
        for direction in DIRECTIONS.keys():
            while direction in map_line:
                carts.append(Cart(map_line, direction, line_number, cart_name))
                cart_name += 1
                if direction in ['<', '>']:
                    map_line = map_line.replace(direction, '-', 1)
                if direction in ['^', 'v']:
                    map_line = map_line.replace(direction, '|', 1)
        return carts, map_line, cart_name

    def advance_tick(self):
        starting_cart_count = len([c for c in self.carts if not c.crashed])
        for cart in self.carts:
            if not cart.crashed:
                x, y = cart.position
                if self.time % 100 == 0:
                    print 'Tick {0} cart ({1},{2}), {3}, {4}'.format(self.time, x, y, self.map[y][x], cart.intersection_behavior)
                cart.advance_tick(self.map[y][x])
                self.detect_collisions()
        self.detect_illegal_movements()
        ending_cart_count = len([c for c in self.carts if not c.crashed])
        if starting_cart_count != ending_cart_count:
            print 'Going from tick {0} to {1}, depleted from {2} carts to {3} carts.'.format(self.time, self.time+1, starting_cart_count, ending_cart_count)
        self.time += 1


    def detect_illegal_movements(self):
        for c in self.carts:
            x, y = c.position
            i, j = c.velocity
            symbol = self.map[y][x]
            if (i != 0 and symbol not in ['-', '\\', '/', '+']) or (j != 0 and symbol not in ['|', '\\', '/', '+']):
                raise RuntimeError('Illegal move')

    def detect_collisions(self):
        positions = [c.position for c in self.carts if not c.crashed]
        duplicates = set([p for p in positions if positions.count(p) > 1])
        if duplicates:
            for c in self.carts:
                if c.position in duplicates:
                    print 'Cart #{0} has crashed at {1}'.format(c.name, c.position)
                    c.crashed = True

    def run_until_collision(self):
        while True:
            self.advance_tick()
            crashed = [c for c in self.carts if c.crashed]
            if crashed:
                print 'Crash detected at {0}'.format(crashed[0].position)
                return

    def run_until_lone_survivor(self):
        while True:
            self.advance_tick()
            uncrashed = [c for c in self.carts if not c.crashed]
            if len(uncrashed) == 1:
                print vars(uncrashed[0])
                return


class Cart(object):
    def __init__(self, map_line, direction, y, name):
        self.name = str(name)
        x = map_line.index(direction)
        self.position = (x, y)
        self.velocity = DIRECTIONS[direction]
        self.intersection_behavior = 'left'
        self.crashed = False
        self.time = 0

    def turn_right(self):
        if self.velocity == DIRECTIONS['^']:
            self.velocity = DIRECTIONS['>']
        elif self.velocity == DIRECTIONS['>']:
            self.velocity = DIRECTIONS['v']
        elif self.velocity == DIRECTIONS['v']:
            self.velocity = DIRECTIONS['<']
        elif self.velocity == DIRECTIONS['<']:
            self.velocity = DIRECTIONS['^']

    def turn_left(self):
        if self.velocity == DIRECTIONS['^']:
            self.velocity = DIRECTIONS['<']
        elif self.velocity == DIRECTIONS['<']:
            self.velocity = DIRECTIONS['v']
        elif self.velocity == DIRECTIONS['v']:
            self.velocity = DIRECTIONS['>']
        elif self.velocity == DIRECTIONS['>']:
            self.velocity = DIRECTIONS['^']

    def handle_intersection(self):
        if self.intersection_behavior == 'left':
            self.turn_left()
            self.intersection_behavior = 'straight'
        elif self.intersection_behavior == 'straight':
            self.intersection_behavior = 'right'
        elif self.intersection_behavior == 'right':
            self.turn_right()
            self.intersection_behavior = 'left'

    def advance_tick(self, track_symbol):
        """Update velocity first based on current position (given), then move in that direction"""
        if track_symbol == '/':
            if self.velocity[0] != 0:
                self.turn_left()
            elif self.velocity[1] != 0:
                self.turn_right()
        elif track_symbol == '\\':
            if self.velocity[0] != 0:
                self.turn_right()
            elif self.velocity[1] != 0:
                self.turn_left()
        elif track_symbol == '+':
            self.handle_intersection()
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.time += 1
        #print 'Cart is at {0} on top of {1}, next move will be towards {2}'.format(self.position, track_symbol, self.velocity)

def part1():
    print ''
    with open('inputs/13_1.txt', 'r') as aoc_input:
        track = Track(aoc_input.read().rstrip('\n').split('\n'))
    track.run_until_collision()
    print ''

def part2():
    print ''
    with open('inputs/13_1.txt', 'r') as aoc_input:
        track = Track(aoc_input.read().rstrip('\n').split('\n'))
    track.run_until_lone_survivor()
    print ''

part1()
part2()
