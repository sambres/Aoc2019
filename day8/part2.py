import math
import time
import re
start_time = time.time()

f = open("./input", "r")
contents = f.read()

width = 25
height = 6

# width = 2
# height = 2

row = []
grid = []
layers = []
for item in contents:
    row.append(int(item))

    if len(row) == width:
        grid.append(row)
        row = []
    if len(grid) == height:
        layers.append(grid)
        grid = []

draw = []
for x in range(height):
    row = []
    for y in range(width):
        for layer in layers:
            if layer[x][y] != 2:
                row.append(layer[x][y])
                break
    draw.append(row)

# print(layers)
print(draw)

s = ''
for x in range(height):
    for y in range(width):
        s += str(draw[x][y])
    s += '\n'

print(s)
print("--- %s seconds ---" % (time.time() - start_time))

# UGCUH

# 1001001100011001001010010
# 1001010010100101001010010
# 1001010000100001001011110
# 1001010110100001001010010
# 1001010010100101001010010
# 0110001110011000110010010
