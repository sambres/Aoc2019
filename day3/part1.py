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

    if(x > max(line1[0][0], line1[1][0]) or x > max(line2[0][0], line2[1][0])):
        return False
    if(x < min(line1[0][0], line1[1][0]) or x < min(line2[0][0], line2[1][0])):
        return False

    if(y > max(line1[0][1], line1[1][1]) or y > min(line2[0][1], line2[1][1])):
        return False
    if(y < min(line1[0][1], line1[1][1]) or y < min(line2[0][1], line2[1][1])):
        return False

    # check that the intersection is IN the segment
    print((x, y))
    return (x, y)


# def print(line1, line2):
#     xMax = max(map(lambda x: x[0], line1 + line2))
#     xMin = min(map(lambda x: x[0], line1 + line1))

#     yMax = max(map(lambda x: x[1], line1 + line2))
#     yMin = min(map(lambda x: x[1], line1 + line1))

#     grid = []
#     for x in range(xMin, xMax):
#         grid.append([])
#         for y in range(yMin, yMax):
#           grid[x].append([])


lines = contents.split('\n')
positions = []
print(lines)
for index in range(2):
    print('line ' + str(index))
    line = lines[index]

    positions.append([[0, 0]])
    moveCount = 0

    for move in lines[index].split(','):
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
        # print([x, y])
print(positions[0])
print(positions[1])


closest = None
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
        if closest == None:
            print(intersect)
            closest = intersect
        if abs(closest[0]) + abs(closest[1]) > abs(intersect[0]) + abs(intersect[1]):
            print(intersect)
            closest = intersect

print(closest)
print(closest[0] + closest[1])

print("--- %s seconds ---" % (time.time() - start_time))
