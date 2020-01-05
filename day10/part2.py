import math
import time
import re
import sys
start_time = time.time()

f = open("./input", "r")
contents = f.read().split('\n')

# epsilon = float_info.epsilon * 10


def man_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def angle(a, b):
    return (math.atan2(a.y-b.y, a.x-b.x))


def is_between(a, c, b):
    part1 = distance(a, c) + distance(c, b)
    part2 = distance(a, b)
    return math.isclose(part1, part2, rel_tol=1e-9)
    # return part1 >= part2 -


def printMeteors(mets):
    grid = ''
    for y, line in enumerate(contents):
        row = ''
        for x, case in enumerate(line):
            m = None
            for meteor in meteors:
                if x == meteor.x and y == meteor.y:
                    m = meteor
                    break
            if m == None:
                row += '.'
            else:
                if m.shot:
                    row += '-'
                else:
                    row += '#'
        grid += row + '\n'
    print(grid)


class Meteor:
    def __init__(self, x, y, id=0, detect=0, angle=0, distance=0, shot=False):
        self.x = x
        self.y = y
        self.id = id
        self.detect = detect
        self.angle = angle
        self.distance = distance
        self.shot = shot

    def __repr__(self):
        return '{ID: ' + str(self.id) + ' x: ' + str(self.x) + ' y: ' + str(self.y) + ' angle: ' + str(self.angle) + ' distance: ' + str(self.distance) + ' shot: ' + str(self.shot) + '}\n'


meteors = []
stationId = 0
for y, line in enumerate(contents):
    for x, case in enumerate(line):
        if case != '.':
            meteors.append(Meteor(x, y, len(meteors)))
        if case == 'X':
            station = meteors[-1]
        #     Meteor.
        #     meteors.append({'x': x, 'y': y, 'id': len(meteors)})


def advance_degrees(deg, advance):
    return ((deg + 180 - advance) % 360) - 180


station = meteors[265]
meteors.remove(station)
angles = {}
for meteor in meteors:
    if meteor.id == station.id:
        continue
    angleRad = angle(station, meteor)
    angleDegrees = advance_degrees(math.degrees(angleRad), 270)
    meteor.angle = angleDegrees
    meteor.distance = man_distance(station, meteor)

    for ang in angles.keys():
        if math.isclose(ang, angleRad, rel_tol=1e-9):
            meteor.angle = angleDegrees

    if angles.get(angleRad):
        angles[angleRad] += 1
    else:
        angles[angleRad] = 1


def sort_by_angle_then_distance(m):
    return (m.angle, m.distance)


meteors.sort(key=sort_by_angle_then_distance)

print(meteors)
# print(angles)
print(len(angles.keys()))

shot = 0
index = 0
while shot < 200 and shot != len(meteors):
    meteor = meteors[index]
    index = (index + 1) % len(meteors)

    if index == 0:
        printMeteors(meteors)

    if meteor.shot:
        continue
    meteor.shot = True
    shot += 1
    print(shot, index, meteor)
    nextM = None
    while True:
        if meteor.angle == meteors[index].angle:
            print('skip', shot)
            index = (index + 1) % len(meteors)
        else:
            break
print(meteors[index])
print(meteors[index - 1])
print(meteors[index - 1].x * 100 + meteors[index - 1].y)

# print(max(map(lambda l: l.detect, meteors)))


printMeteors(meteors)

print("--- %s seconds ---" % (time.time() - start_time))
