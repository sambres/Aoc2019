import math
import time
start_time = time.time()

f = open("input", "r")
contents = f.read()


class Planet:

    def __init__(self, name, orbited):
        self.orbited = orbited
        self.orbits = []
        self.name = name

    def __repr__(self):
        return self.name + ')' + ','.join(map(lambda x: x.name, self.orbits)) + ((self.orbited and '[' + self.orbited.name + ']') or '')


def findPlanet(planets, root, search, count=0, previous=None):
    if root.name == search:
        print('here', count)
        return count
    for p in root.orbits + [root.orbited]:
        if p.name not in planetsDic or (previous and p.name == previous.name):
            continue
        found = findPlanet(planets, p, search, count + 1, root)
        if found:
            return found
    return 0


def searchSanta(orbits, planet, origin, count=0):
    print('planet', planet, origin)
    if planet[0] == 'SAN' or planet[1] == 'SAN':
        return (True, count)
    planet.append(True)
    for p in filter(lambda o: len(o) < 3, orbits):
        if p[1] == planet[0] and p[1] != origin:
            resultR, rcount = searchSanta(orbits, p, p[1], count + 1)
            print('resultR', resultR)
            if resultR:
                return (resultR, rcount)

        if p[0] == planet[1] and p[0] != origin:
            resultL, lcount = searchSanta(orbits, p, p[0], count + 1)
            print('resultL', resultL)
            if resultL:
                return (resultL, lcount)
    return (False, count)


array = contents.split('\n')

you = None
santa = None
orbits = []
planetsDic = {}
for orbit in array:
    print('orbit', orbit)
    couple = orbit.split(')')

    orbited = None
    if couple[0] in planetsDic:
        orbited = planetsDic[couple[0]]
    else:
        orbited = Planet(couple[0], None)
        planetsDic[orbited.name] = orbited

    orbiting = None
    if couple[1] in planetsDic:
        orbiting = planetsDic[couple[1]]
        orbiting.orbited = orbited
    else:
        orbiting = Planet(couple[1], orbited)
        planetsDic[orbiting.name] = orbiting

    orbited.orbits.append(orbiting)

santa = planetsDic['SAN'].orbited
you = planetsDic['YOU'].orbited

planets = list(planetsDic.values())

print(planets)

res = findPlanet(planetsDic, you, santa.name)
print(res)

print("--- %s seconds ---" % (time.time() - start_time))
