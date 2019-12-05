class Coord(object):
    def __init__(self, t):
        self.x = t[0]
        self.y = t[1]
        self.val = t
    
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
    
    def __lt__(self, other):
        return self.y < other.y or (self.y == other.y and self.x < other.x)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, t):
        return (self.x + t[0], self.y + t[1])

def play_round():
    for active_player in get_active_player():
        cave[active_player.coord.val] = '.'

        legal_targets = [t for t in units if t.hp > 0 and t.letter != active_player.letter]
        if not legal_targets:
            # If there are no more legal targets, the game ends.
            exit(1)

        in_range_spaces = []
        for target in legal_targets:
            in_range_spaces.extend(get_in_range_spaces(target))
        if not in_range_spaces:
            # No unengaged enemies; end active player's turn
            continue
        else:
            in_range_spaces.sort()
        
        reachable_spaces = is_reachable(in_range_spaces)
        
        # Now determine if we move.
        for space in in_range_spaces:
            if space == active_player.position:
                pass

        cave[active_player.coord.val] = active_player.letter

def get_active_player():
    for unit in sorted(units, key=lambda x: x.coord):
        yield unit

def get_in_range_spaces(target):
    return [c for c in target.coord + (-1, 0), target.coord + (1, 0), target.coord + (0, -1), target.coord + (0, 1) if cave[c] == '.']

def is_reachable(spaces):
    for space in spaces:


class Elf(object):
    def __init__(self, coord):
        self.coord = coord
        self.atk = 3
        self.hp = 200
        self.round = 0
        self.letter = 'E'

class Goblin(object):
    def __init__(self, coord):
        self.coord = coord
        self.atk = 3
        self.hp = 200
        self.round = 0
        self.letter = 'G'

cave = {}
units = []
with open('inputs/15_1.txt', 'r') as aoc_input:
    lines = aoc_input.read().rstrip('\n').split('\n')
    for y, line in enumerate(lines, 1):
        for x, letter in enumerate(list(line), 1):
            c = Coord((x, y))
            cave.update({(x, y): letter})
            if letter == 'E':
                units.append(Elf(c))
            elif letter == 'G':
                units.append(Goblin(c))

play_round()