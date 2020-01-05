# from day5.part1 import intCode
from intcode import intCode
from itertools import permutations
import time
import math

start_time = time.time()

f = open("input", "r")
contents = f.read()
array = contents.split(',')

# phases = [4, 3, 2, 1, 0]
phases = list(map(list, permutations(range(5), 5)))
# print(len(phases))
idealPhase = None
maxOutput = 0
for phase in phases:
    output = 0
    for index, thruster in enumerate(['A', 'B', 'C', 'D', 'E']):
        output = intCode(array, [output, phase[index]])
    print(phase, output)
    if int(output) > maxOutput:
        idealPhase = phase
        maxOutput = int(output)

print('final', maxOutput, idealPhase)

print("--- %s seconds ---" % (time.time() - start_time))
