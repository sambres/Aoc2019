# from day5.part1 import intCode
from intcode import intCode
from itertools import permutations
import time

start_time = time.time()

f = open("input", "r")
contents = f.read()
array = contents.split(',')

# phases = [[1, 0, 4, 3, 2]]
phases = list(map(list, permutations(range(5), 5)))
# print(len(phases))
idealPhase = None
maxOutput = 0
for phase in phases:
    output = 0
    for index, thruster in enumerate(['A', 'B', 'C', 'D', 'E']):
        output = intCode(array, [phase[index], output])
    # print(phase, output)
    if int(output) > maxOutput:
        idealPhase = phase
        maxOutput = int(output)

print('final', maxOutput, idealPhase)

print("--- %s seconds ---" % (time.time() - start_time))
