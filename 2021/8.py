#! /usr/bin/env python3

def a():
    return set([d for d in digits if len(d) == 3][0]) - set([d for d in digits if len(d) == 2][0])

def b():
    return get_by_count(6)

def c():
    return get_by_count(8) - a()

def d():
    return set([d for d in digits if len(d) == 4][0]) - set([d for d in digits if len(d) == 2][0]) - b()

def e():
    return get_by_count(4)

def f():
    return get_by_count(9)

def g():
    return get_by_count(7) - d()

def get_by_count(n):
    return set({s for s, count in segment_incidence.items() if count == n})

total_result = 0
with open('8.txt', 'r') as infile:
    for line in infile.readlines():
        line = line.strip().upper()
        patterns, outputs = line.split('|')

        digits = [sorted(list(digit)) for digit in patterns.split()]
        segment_incidence = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
        for digit in digits:
            for segment in digit:
                segment_incidence[segment] += 1

        tr = outputs[:]
        tr = tr.replace(''.join(a()), 'a')
        tr = tr.replace(''.join(b()), 'b')
        tr = tr.replace(''.join(c()), 'c')
        tr = tr.replace(''.join(d()), 'd')
        tr = tr.replace(''.join(e()), 'e')
        tr = tr.replace(''.join(f()), 'f')
        tr = tr.replace(''.join(g()), 'g')
        
        result = ''
        for digit in tr.split():
            s = set(list(digit))
            if   s == set(['a', 'b', 'c',      'e', 'f', 'g']):
                dx = '0'
            elif s == set([          'c',           'f'     ]):
                dx = '1'
            elif s == set(['a',      'c', 'd', 'e',      'g']):
                dx = '2'
            elif s == set(['a',      'c', 'd',      'f', 'g']):
                dx = '3'
            elif s == set([     'b', 'c', 'd',      'f',    ]):
                dx = '4'
            elif s == set(['a', 'b',      'd',      'f', 'g']):
                dx = '5'
            elif s == set(['a', 'b',      'd', 'e', 'f', 'g']):
                dx = '6'
            elif s == set(['a',      'c',           'f',    ]):
                dx = '7'
            elif s == set(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
                dx = '8'
            else:
                dx = '9'
            result = result + dx
        total_result += int(result)
print(total_result)
