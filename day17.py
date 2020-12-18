import numpy as np
import pandas as pd

data = open('day17.txt').read().split('\n')

# x y z
# row, col, layer
active = []
z = 0
x = 0
for row in data:
    y = 0
    for col in row:
        if col == '#':
            point = (x, y, z)
            active.append(point)
        y += 1
    x += 1

def make_block(x, y, z):
    x_range = [x-1, x, x+1]
    y_range = [y-1, y, y+1]
    z_range = [z-1, z, z+1]

    block = []
    for i in x_range:
        for j in y_range:
            for k in z_range:
                cube = (i, j, k)
                block.append(cube)
    block.remove((x,y,z))

    return block

# part 1
for cycle in range(0,6):
    max_column = max([abs(tup[1]) for tup in active]) +1
    max_row = max([abs(tup[0]) for tup in active]) +1
    max_layer = max([abs(tup[2]) for tup in active]) +1

    columns = range(-max_column, max_column+1)
    rows = range(-max_row, max_row+1)
    layers = range(-max_layer, max_layer+1)

    new_active = []
    for z in layers:
        for x in rows:
            for y in columns:
                block = make_block(x,y,z)
                active_in_block = len(set(block) & set(active))
                # print(active_in_block)
                if (x,y,z) in active:
                    if active_in_block == 2 or active_in_block == 3:
                        new_active.append((x, y, z))
                else:
                    if active_in_block == 3:
                        new_active.append((x, y, z))
    # print(active)
    active = new_active

print(len(active))
    