import math
import time
start_time = time.time()
f = open("input", "r")


def computeFuel(module):
    fuel = math.floor(int(module) / 3) - 2
    # print(fuel)
    if fuel > 0:
        ff = computeFuel(fuel)
        if ff > 0:
            fuel += ff

    return fuel


contents = f.read()
sum = 0
for module in contents.split('\n'):
    mass = computeFuel(module)
    print(mass)
    sum += mass
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
