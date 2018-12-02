
with open('inputs/2_1.txt', 'r') as aoc_input:
    box_ids = aoc_input.read().rstrip('\n').split('\n')

# PART 1

num_exactly_two = 0
num_exactly_three = 0

for identifier in box_ids:
    letter_counts = {}
    for letter in identifier:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    if 2 in letter_counts.values():
        num_exactly_two += 1
    if 3 in letter_counts.values():
        num_exactly_three += 1

print num_exactly_two * num_exactly_three

# PART 2

def difference_between_two_ids(a, b):
    return sum([1 for i, j in zip(a, b) if i != j])

def find_ids_exactly_one_apart(box_ids):
    for i, id1 in enumerate(box_ids, 0):
        for id2 in box_ids[i+1:]:
            if difference_between_two_ids(id1, id2) == 1:
                return id1, id2
                
print find_ids_exactly_one_apart(box_ids)