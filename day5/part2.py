import math
import time
start_time = time.time()

f = open("input", "r")
array = f.read().split(',')
input = 5

# print(array)

i = 0
while True:
    step = 0
    print('op', array[i])
    op = int(array[i][-2:])
    if op == 99:
        break

    if op == 1 or op == 2 or op == 7 or op == 8:
        parametersLength = 3
    if op == 3 or op == 4:
        parametersLength = 1
    if op == 5 or op == 6:
        parametersLength = 2

    modes = array[i][:-2].zfill(parametersLength)
    parameters = []
    for index, mode in enumerate(modes[::-1]):
        parameter = int(array[i + index + 1])
        if mode == '0':
            # position
            parameters.append(parameter)
        else:
            # immediate
            parameters.append(i + index + 1)

    # print(parameters)

    if op == 1:
        array[parameters[2]] = str(
            int(array[parameters[0]]) + int(array[parameters[1]]))
    if op == 2:
        array[parameters[2]] = str(
            int(array[parameters[0]]) * int(array[parameters[1]]))
    if op == 3:
        array[parameters[0]] = str(input)
    if op == 4:
        input = array[parameters[0]]
        print('newinput', parameters[0], array[parameters[0]])

    if op == 5 and array[parameters[0]] != '0':
        print('5', parameters)
        i = int(array[parameters[1]])
        continue
    if op == 6 and array[parameters[0]] == '0':
        print('6', parameters)
        i = int(array[parameters[1]])
        continue

    if op == 7:
        if array[parameters[0]] < array[parameters[1]]:
            array[parameters[2]] = '1'
        else:
            array[parameters[2]] = '0'
    if op == 8:
        if array[parameters[0]] == array[parameters[1]]:
            array[parameters[2]] = '1'
        else:
            array[parameters[2]] = '0'

    i += parametersLength + 1
    # print(array)
print('input', input)

print("--- %s seconds ---" % (time.time() - start_time))
