with open('inputs/7_1.txt', 'r') as aoc_input:
    requirements = [(instruction.split()[1], instruction.split()[7]) for instruction in aoc_input.read().rstrip().split('\n')]

class Step(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, Step):
        self.children.append(Step)

    def add_parent(self, Step):
        self.parents.append(Step)
    
def initialize():
    step_map = {}
    for s in set([r[0] for r in requirements] + [r[1] for r in requirements]):
        step_map[s] = Step(s)
    for parent, child in requirements:
        step_map[parent].add_child(child)
        step_map[child].add_parent(parent)
    return step_map

step_map = initialize()
solution = ''
while step_map:
    chosen = sorted([s.name for s in step_map.values() if not s.parents])[0]
    solution += chosen
    for child in step_map[chosen].children:
        step_map[child].parents.remove(chosen)
    del step_map[chosen]
print solution

step_map = initialize()
free_elves = [None] * 5
working_elves = []
total_time = 0
while step_map or working_elves:
    unblocked_steps = sorted([s.name for s in step_map.values() if not s.parents])
    if free_elves and unblocked_steps:
        for worker, step in zip(free_elves, unblocked_steps):
            #print 'Assigning an idle elf to work on {0} for {1} seconds'.format(step, 60+ord(step)-64)
            free_elves.pop()
            working_elves.append((step_map[step], 60 + ord(step) - 64))
            del step_map[step]
    else:
        #print 'Advance time!!!'
        working_elves = [(w[0], w[1]-1) for w in working_elves]
        total_time += 1
        for worker in working_elves:
            if worker[1] == 0:
                #print 'Task {0} complete!'.format(worker[0].name)
                for child in worker[0].children:
                    step_map[child].parents.remove(worker[0].name)
                free_elves.append(None)
        working_elves = [(w[0], w[1]) for w in working_elves if w[1] > 0]
print total_time