#! /usr/bin/env python

with open('inputs/12_1.txt', 'r') as aoc_input:
    lines = aoc_input.read().rstrip('\n').split('\n')

def advance(starting, rules, shortcuts):
    starting_string = ''.join(starting)
    if starting_string in shortcuts:
        shortcut = shortcuts[starting_string]
        return shortcut[0], shortcut[1], shortcuts, 1
    rule_size = len(rules.keys()[0])
    half_rule = (rule_size - 1)/2
    padded = ['.']*(rule_size - 1) + starting + ['.']*(rule_size - 1)
    ending = []
    length = len(padded)
    for i in xrange(0, length - rule_size + 1):
        key = ''.join(padded[i:i+rule_size])
        if key in rules:
            ending.append(rules[key])
        else:
            ending.append('.')
    first_plant = ending.index('#')
    last_plant = list(reversed(ending)).index('#')
    shortcuts[starting_string] = (ending[first_plant:-last_plant], first_plant)
    return ending[first_plant:-last_plant], first_plant, shortcuts, 0

state = list(lines[0].split(' ')[2])
rules = {}
for line in lines[2:]:
    key, value = line.split(' => ')
    rules[key] = value

max_generations = 50000000000
generation = 0
total_adjustment = 0
shortcuts = {}
shortcut_count = 0
power_of_ten = 10
cycle = ([], generation)
#print 0, ' '*2*(max_generations-generation) + ''.join(state)
while generation < max_generations:
    if generation % power_of_ten == 0:
        #print 'Hit generation {0}: {1}, {2}'.format(generation, len(state), shortcut_count)
        if shortcut_count == power_of_ten:
            cycle = (state, generation)
        shortcut_count = 0

    state, adjustment, shortcuts, used_shortcut = advance(state, rules, shortcuts)
    generation += 1
    total_adjustment += adjustment
    shortcut_count += used_shortcut

    if state == cycle[0]:
        print 'Detected a cycle spanning from gen #{0} to gen #{1}, shortcutting rest of simulation'.format(cycle[1], generation)
        cycles_to_finish = (max_generations - generation) / (generation - cycle[1])
        total_adjustment += adjustment * cycles_to_finish
        generation = max_generations - 1
        break
    #print (generation+1)%10, ' '*(total_adjustment+(max_generations-generation-1)*2)+''.join(state)

total = 0
for i in xrange(0, len(state)):
    if state[i] == '#':
        total += (i - (2 * generation+2)) + total_adjustment
print total
