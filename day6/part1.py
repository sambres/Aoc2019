import math
import time
start_time = time.time()

f = open("input", "r")
contents = f.read()


def countOrbit(planet, orbits):
    count = 0
    for index, orbit in enumerate(orbits):
        if orbit[1] == planet:
            count += 1
            count += countOrbit(orbit[0], orbits)
    return count


array = contents.split('\n')

orbits = []
planetsDic = {}
for orbit in array:
    print('orbit', orbit)
    orbits.append(orbit.split(')'))
    planetsDic[orbits[-1][0]] = 1
    planetsDic[orbits[-1][1]] = 1

print(orbits)
planets = list(planetsDic.keys())

print(planets)

sum = 0
for planet in planets:
    count = countOrbit(planet, orbits)
    print(planet, count)
    sum += count

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))
