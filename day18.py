forest = {}
with open('inputs/18_1.txt', 'r') as aoc_input:
    y_max = 0
    for y, line in enumerate(aoc_input.read().rstrip('\n').split('\n'), 0):
        x_max = 0
        y_max += 1
        for x, letter in enumerate(list(line), 0): 
            forest[(x, y)] = letter
            x_max += 1
    
history = {}
max_iter = 1000000000
it = 0
while it < max_iter:
    new_forest = {}
    done = False
    for x, y in [coord for coord, current in forest.items() if current == '.']:
        current = forest[(x, y)]
        tree_acre = 0
        for adjacent in [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]:
            try:
                if forest[adjacent] == '|':
                    tree_acre += 1
            except KeyError:
                pass
            if tree_acre >= 3:
                new_forest[(x, y)] = '|'
                break
    for x, y in [coord for coord, current in forest.items() if current == '|']:
        current = forest[(x, y)]
        lumberyard = 0
        for adjacent in [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]:
            try:
                if forest[adjacent] == '#':
                    lumberyard += 1
            except KeyError:
                pass
            if lumberyard >= 3:
                new_forest[(x, y)] = '#'
                break
    for x, y in [coord for coord, current in forest.items() if current == '#']:
        current = forest[(x, y)]
        lumberyard = 0
        tree_acre = 0
        for adjacent in [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]:
            try:
                if forest[adjacent] == '#':
                    lumberyard += 1
                elif forest[adjacent] == '|':
                    tree_acre += 1
            except KeyError:
                pass
        if not (lumberyard >= 1 and tree_acre >= 1):
            new_forest[(x, y)] = '.'
    if len(new_forest.keys()) == 0:
        break
    forest.update(new_forest)
    if sorted(forest.items()) in history.values():
        period = it - history.values().index(sorted(forest.items()))
        #print 'Detected a loop of size {0}'.format(period)
        #print 'Skipping from {0} to {1}'.format(it, it + period * int((max_iter - it ) / period))
        it = it + period * int((max_iter - it) / period) + 1
        continue
    history[it] = sorted(forest.items())
    it += 1

print len([l for l in forest.values() if l == '|']), len([l for l in forest.values() if l == '#']), len([l for l in forest.values() if l == '.'])
print len([l for l in forest.values() if l == '|']) * len([l for l in forest.values() if l == '#'])