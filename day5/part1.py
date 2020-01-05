import math
import time
start_time = time.time()

f = open("input", "r")
contents = f.read()

array = contents.split(',')


def intCode(program, input):
    i = 0
    result = input
    while True:
        print('op', program[i])
        op = int(program[i][-2:])
        if op == 99:
            return result

        parametersLength = 3 if op == 1 or op == 2 else 1
        modes = program[i][:-2].zfill(parametersLength)
        parameters = []
        for index, mode in enumerate(modes[::-1]):
            parameter = int(program[i + index + 1])
            if mode == '0':
                # position
                parameters.append(parameter)
            else:
                # immediate
                parameters.append(i + index + 1)

        if op == 1:
            program[parameters[2]] = str(
                int(program[parameters[0]]) + int(program[parameters[1]]))

        if op == 2:
            program[parameters[2]] = str(
                int(program[parameters[0]]) * int(program[parameters[1]]))
        if op == 3:
            program[parameters[0]] = str(result)
        if op == 4:
            result = program[parameters[0]]
            print('newresult', parameters[0], program[parameters[0]])
        i += parametersLength + 1


print('result', intCode(array, 1))


print("--- %s seconds ---" % (time.time() - start_time))
