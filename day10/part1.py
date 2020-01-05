import math
import time
import re
import sys
start_time = time.time()

f = open("./example", "r")
contents = f.read().split('\n')

# epsilon = float_info.epsilon * 10


def distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def is_between(a, c, b):
    part1 = distance(a, c) + distance(c, b)
    part2 = distance(a, b)
    return math.isclose(part1, part2, rel_tol=1e-9)
    # return part1 >= part2 -


class Meteor:
    def __init__(self, x, y, id=0, detect=0):
        self.x = x
        self.y = y
        self.id = id
        self.detect = detect

    def __repr__(self):
        return '{ID: ' + str(self.id) + ' x: ' + str(self.x) + ' y: ' + str(self.y) + ' detect: ' + str(self.detect) + '}\n'


meteors = []
for y, line in enumerate(contents):
    for x, case in enumerate(line):
        if case != '.':
            meteors.append(Meteor(x, y, len(meteors)))
print(meteors)

for index1, meteor1 in enumerate(meteors[:-1]):  # except last element
    detect = 0
    print(meteor1, "--- %s seconds ---" % (time.time() - start_time))
    for index2, meteor2 in enumerate(meteors[index1+1:]):
        isBetween = False
        if meteor2.id == meteor1.id:
            continue
        for index3, meteor3 in enumerate(meteors):
            if meteor3.id == meteor1.id or meteor3.id == meteor2.id:
                continue
            pass
            if is_between(meteor1, meteor3, meteor2):
                isBetween = True
                break
        if isBetween == True:
            continue
        meteor1.detect += 1
        meteor2.detect += 1

print(meteors)
print(max(map(lambda l: l.detect, meteors)))

print("--- %s seconds ---" % (time.time() - start_time))

# {ID: 265 x: 26 y: 29 detect: 299}
