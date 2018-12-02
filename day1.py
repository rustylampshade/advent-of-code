
# PART 1

with open('inputs/1_1.txt', 'r') as aoc_input:
    frequency_changes = aoc_input.read().rstrip('\n').split('\n')

starting_freq = 0
for change in frequency_changes:
    starting_freq += int(change)

print starting_freq

# PART 2

def find_repeated_intermediate_freq():
    intermediate_freqs = {}
    starting_freq = 0
    #seen_freqs = 0
    while True:
        for change in frequency_changes:
            starting_freq += int(change)
            #seen_freqs += 1
            if starting_freq in intermediate_freqs:
                #print "Found after {0} seen frequencies!".format(seen_freqs)
                return starting_freq
            intermediate_freqs[starting_freq] = True

print find_repeated_intermediate_freq()