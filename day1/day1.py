import math
import time
start_time = time.time()

f = open("input", "r")


def computeFuel(module):
    return math.floor(int(module) / 3) - 2


contents = f.read()
sum = 0
for module in contents.split('\n'):
    mass = computeFuel(module)
    sum += mass
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
