#! /usr/bin/env python3

from collections import Counter
with open('6.txt', 'r') as infile:
    start = Counter(map(int, infile.read().strip().split(',')))

def nextday(current_counts):
    upcoming_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for timer, count in current_counts.items():
        if timer > 0:
            upcoming_counts[timer - 1] += count
        if timer == 0:
            upcoming_counts[8] = count
            upcoming_counts[6] += count
    return upcoming_counts

today = start
for i in range(0, 256):
    today = nextday(today)

print(sum([value for value in today.values()]))
