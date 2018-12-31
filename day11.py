#! /usr/bin/env python 

def calculate_power_grid(grid_size, serial, desired=None):
    powers = [[]]
    for x in range(1, grid_size + 1):
        powers.append([0] * (grid_size + 1))
        for y in range(1, grid_size + 1):
            rack_id = x + 10
            powers[x][y] = int(str(((rack_id * y) + serial) * rack_id)[-3]) - 5
    if desired:
        print 'The power of {0} with serial {1} is: {2}'.format(desired, serial, powers[desired[0]][desired[1]])
    return powers

def find_largest_box(box_size, grid):
    grid_size = len(grid)
    largest_box = (None, -1e6, box_size)
    i = 1
    while i <= grid_size - box_size:
        j = 1
        while j <= grid_size - box_size:
            total_power = 0
            for x in range(i, i + box_size):
                total_power += sum(grid[x][j:j+box_size])
            if total_power > largest_box[1]:
                largest_box = ((i, j), total_power, box_size)
            j += 1
        i += 1
    print largest_box


#####
# Tests
######

#calculate_power_grid(5, 8, (3,5))
#calculate_power_grid(122, 57, (122,79))
#calculate_power_grid(217, 39, (217,196))
#calculate_power_grid(153, 71, (101,153))
#grid = calculate_power_grid(300, 18)
#find_largest_box(3, grid)
#grid = calculate_power_grid(300, 42)
#find_largest_box(3, grid)


grid = calculate_power_grid(300, 3613)
for size in range(1, 301):
    find_largest_box(size, grid)

