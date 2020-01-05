import math
import time
start_time = time.time()

f = open("./input", "r")
contents = f.read()


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    if is_between(line1[0], (x, y), line1[1]) and is_between(line2[0], (x, y), line2[1]):
        return (x, y)
    return False


def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def is_between(a, c, b):
    return distance(a, c) + distance(c, b) == distance(a, b)


lines = list(map(lambda l: l.split(','), contents.split('\n')))
positions = []
for index in range(2):
    # print('line ' + str(index))
    line = lines[index]

    positions.append([[0, 0]])
    moveCount = 0

    for move in lines[index]:
        position = positions[index][moveCount]

        dir = move[0]
        norm = int(move[1:])
        x = position[0]
        y = position[1]

        if dir == 'R':
            x += norm

        if dir == 'L':
            x -= norm

        if dir == 'U':
            y += norm

        if dir == 'D':
            y -= norm

        positions[index].append([x, y])
        moveCount += 1


intersections = []
for moveIndex in range(len(positions[0]) - 1):
    A = positions[0][moveIndex]
    B = positions[0][moveIndex + 1]
    for otherMoveIndex in range(len(positions[1]) - 1):
        C = positions[1][otherMoveIndex]
        D = positions[1][otherMoveIndex + 1]
        # print(A, B, C, D)

        intersect = line_intersection((A, B), (C, D))
        if intersect == False or (intersect[0] == 0 and intersect[1] == 0):
            continue
        intersections.append(intersect)

print('closest', intersections)

distances = list(map(lambda i: [0, 0],  range(len(intersections))))
for lineIndex in range(len(positions)):
    path = positions[lineIndex]
    line = lines[lineIndex]
    for interIndex in range(len(intersections)):
        for moveIndex in range(len(path) - 1):
            intersection = intersections[interIndex]

            if is_between(path[moveIndex], intersection, path[moveIndex + 1]):
                distances[interIndex][lineIndex] += distance(
                    path[moveIndex], intersection)
                break
            distances[interIndex][lineIndex] += int(line[moveIndex][1:])

print('distances', distances, min(map(lambda x: x[0] + x[1], distances)))


print("--- %s seconds ---" % (time.time() - start_time))
