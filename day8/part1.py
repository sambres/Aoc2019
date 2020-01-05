import math
import time
import re
start_time = time.time()

f = open("./input", "r")
contents = f.read()

width = 25
height = 6

# width = 3
# height = 2

row = []
layers = []
minZeros = None
goodLayer = None
for item in contents:
    row.append(int(item))

    if len(row) == width * height:
        # layers.append(row)
        zeros = row.count(0)
        if minZeros == None or minZeros > zeros:
            minZeros = zeros
            goodLayer = row
        row = []


print(goodLayer, minZeros, goodLayer.count(1), goodLayer.count(
    2), goodLayer.count(1) * goodLayer.count(2))

print("--- %s seconds ---" % (time.time() - start_time))
