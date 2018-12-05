import string

with open('inputs/5_1.txt', 'r') as aoc_input:
    orig = list(aoc_input.read().rstrip('\n'))

def fully_react(chain):
    i = 0
    while i < len(chain) - 1:
        # For some reason, the cases aren't separated by only 26 points but there are also six punctuation symbols between.
        if abs(ord(chain[i]) - ord(chain[i+1])) == 32:
            del(chain[i+1])
            del(chain[i])
            if i != 0:
                i -=1
            continue
        i += 1
    return chain
    
print len(fully_react(orig[:]))

reaction_sizes = {}
for letter in string.ascii_lowercase:
    modified = list(''.join(orig).replace(letter, '').replace(letter.upper(), ''))
    reaction_sizes[letter] = len(fully_react(modified))
print min(reaction_sizes, key=reaction_sizes.get)