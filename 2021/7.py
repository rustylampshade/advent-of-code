#! /usr/bin/env python3

with open('7.txt', 'r') as infile:
    crabs = [int(n) for n in infile.read().strip().split(',')]

def gauss(n):
    return (n+1)*n/2

part1 = {}
part2 = {}
for i in range(min(crabs), max(crabs)):
    part1[i] = sum([abs(n - i) for n in crabs])
    part2[i] = sum([gauss(abs(n - i)) for n in crabs])

print(min(part1.values()))
print(min(part2.values()))
