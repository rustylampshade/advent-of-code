with open('inputs/5_1.txt', 'r') as aoc_input:
    orig = [ord(letter) for letter in aoc_input.read().strip()]

def fully_react(chain):
    i = 0
    finish = len(chain) - 1
    while i < finish:
        # For some reason, the cases aren't separated by only 26 points but there are also six punctuation symbols between.
        diff = chain[i] - chain[i+1]
        if diff == 32 or diff == -32:
            del(chain[i+1])
            del(chain[i])
            finish -= 2
            if i != 0:
                i -=1
            continue
        i += 1
    return chain
    
print len(fully_react(orig))

reaction_sizes = {}
for upper, lower in zip(range(65, 91), range(97, 123)):
    reaction_sizes[upper] = len(fully_react([l for l in orig if l != lower and l != upper]))
print min(reaction_sizes.values())