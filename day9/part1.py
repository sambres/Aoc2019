# from day5.part1 import intCode
from intcode import intCodeAdvance
from itertools import permutations
import time

start_time = time.time()

f = open("input", "r")
contents = f.read()
array = contents.split(',')

print(intCodeAdvance(array, [1]))

print("--- %s seconds ---" % (time.time() - start_time))
