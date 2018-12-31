registers = [0] * 4
op_map = {}

def addr(a, b, c):
    registers[c] = add(registers[a], registers[b])
def addi(a, b, c):
    registers[c] = add(registers[a], b)
def add(a, b):
    return a + b

def mulr(a, b, c):
    registers[c] = mul(registers[a], registers[b])
def muli(a, b, c):
    registers[c] = mul(registers[a], b)
def mul(a, b):
    return a * b

def banr(a, b, c):
    registers[c] = ban(registers[a], registers[b])
def bani(a, b, c):
    registers[c] = ban(registers[a], b)
def ban(a, b):
    return a & b

def borr(a, b, c):
    registers[c] = bor(registers[a], registers[b])
def bori(a, b, c):
    registers[c] = bor(registers[a], b)
def bor(a, b):
    return a | b

def setr(a, b, c):
    registers[c] = registers[a]
def seti(a, b, c):
    registers[c] = a

def gtir(a, b, c):
    registers[c] = gt(a, registers[b])
def gtri(a, b, c):
    registers[c] = gt(registers[a], b)
def gtrr(a, b, c):
    registers[c] = gt(registers[a], registers[b])
def gt(a, b):
    return 1 if a > b else 0

def eqir(a, b, c):
    registers[c] = eq(a, registers[b])
def eqri(a, b, c):
    registers[c] = eq(registers[a], b)
def eqrr(a, b, c):
    registers[c] = eq(registers[a], registers[b])
def eq(a, b):
    return 1 if a == b else 0

with open('inputs/16_1.txt', 'r') as aoc_input:
    stage = 0
    samples = 0
    sample_with_three_options = 0
    for line in aoc_input.read().rstrip('\n').split('\n'):
        if line.startswith('Before:'):
            in_registers = [int(val.strip()) for val in line.split(' ', 1)[1].strip('[]').split(',')]
            samples += 1
            stage = 1
            #print 'Before line -> {0}'.format(in_registers)
        elif stage == 1:
            opcode, a, b, c = [int(val) for val in line.split(' ')]
            # COMMENT OUT FOR PART 1
            if opcode not in op_map:
                op_map[opcode] = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
            # COMMENT OUT FOR PART 2
            #op_map[opcode] = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
            stage = 2
            #print 'Middle line -> {0}, {1}, {2}, {3}'.format(opcode, a, b, c)
        elif stage == 2:
            out_registers = [int(val.strip()) for val in line.split(' ', 2)[2].strip('[]').split(',')]
            for op in op_map[opcode][:]:
                registers = in_registers[:]
                op(a, b, c)
                #print 'When using {0}, registers go from {1} to {2}'.format(op, in_registers, registers)
                if registers != out_registers:
                    op_map[opcode].remove(op)
            if len(op_map[opcode]) >= 3:
                sample_with_three_options += 1
            stage = 0

identified = {}
while op_map.keys():
    for k in op_map.keys():
        v = op_map[k][:]
        if len(v) == 1:
            func = v[0]
            identified[k] = func
            for op in op_map.keys():
                try:
                    op_map[op].remove(func)
                except ValueError:
                    pass
                if len(op_map[op]) == 0:
                    del op_map[op]

print identified

with open('inputs/16_1.txt', 'r') as aoc_input:
    huge_str = aoc_input.read()
    program = huge_str[huge_str.index('\n\n\n'):]
    registers = [0, 0, 0, 0]
    for line in program.strip('\n').split('\n'):
        opcode, a, b, c = [int(val) for val in line.split(' ')]
        identified[opcode](a, b, c)
    print registers