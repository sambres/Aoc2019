import math
import time
start_time = time.time()

f = open("input", "r")
contents = f.read()

puzzle = []
for op in contents.split(','):
    puzzle.append(int(op))

print(puzzle)


for noun in range(99):
    for verb in range(99):
        array = puzzle.copy()
        array[1] = noun
        array[2] = verb

        i = 0
        cpt = 0
        while True:
            op = array[i]
            if op == 99:
                break

            input1 = array[i + 1]
            input2 = array[i + 2]
            input3 = array[i + 3]

            if op == 1:
                array[input3] = array[input1] + array[input2]
            else:
                array[input3] = array[input1] * array[input2]
            # print(cpt)
            cpt += 1
            i += 4

        if array[0] == 19690720:
            break
    if array[0] == 19690720:
        break

print(noun, verb, array[0], noun * 100 + verb)

print("--- %s seconds ---" % (time.time() - start_time))
