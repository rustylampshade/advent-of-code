#! /usr/bin/env python3

with open('4.txt', 'r') as infile:
    lines = list(map(str.strip, infile.readlines()))
    numbers = lines[0].split(',')
    bingo = []
    for i in range(0, int((len(lines) - 1)/6)):
        card = [l.split() for l in lines[2+i*6 : 2+i*6+5]]
        bingo.append(card)

def sum_unmarked(narray, card):
    s = 0
    for row in card:
        for number in row:
            if number not in narray:
                s += int(number)
    return s

def call_numbers(narray, cardset):
    for card in cardset:
        for row in card:
            if all([n in narray for n in row]):
                return sum_unmarked(narray, card) * int(narray[-1]), len(narray)
        for i in range(0, 5):
            column = [r[i] for r in card]
            if all([n in narray for n in column]):
                return sum_unmarked(narray, card) * int(narray[-1]), len(narray)
    return False, False

# Part 1
for i in range(1, len(numbers)):
    score, winning_round = call_numbers(numbers[0:i], bingo)
    if score:
        print('Part 1: %s' % score)
        break

# Part 2
results = []
for card in bingo:
    for i in range(1, len(numbers)):
        score, winning_round = call_numbers(numbers[0:i], [card])
        if score:
            results.append([score, winning_round])
            break
print('Part 2: %s' % ([r[0] for r in results if r[1] == max([r[1] for r in results])][0]))
