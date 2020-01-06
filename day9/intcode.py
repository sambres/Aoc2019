
def intCode(program, input):
    result = None
    i = 0
    while True:
        # print('op', program[i])
        op = int(program[i][-2:])
        if op == 99:
            return result

        if op == 1 or op == 2 or op == 7 or op == 8:
            parametersLength = 3
        if op == 3 or op == 4:
            parametersLength = 1
        if op == 5 or op == 6:
            parametersLength = 2

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
            program[parameters[0]] = str(input.pop(0))
        if op == 4:
            result = program[parameters[0]]
            # print('newinput', parameters[0], program[parameters[0]])

        if op == 5 and program[parameters[0]] != '0':
            # print('5', parameters, program[parameters[1]])
            i = int(program[parameters[1]])
            continue
        if op == 6 and program[parameters[0]] == '0':
            # print('6', parameters)
            i = int(program[parameters[1]])
            continue

        if op == 7:
            if program[parameters[0]] < program[parameters[1]]:
                program[parameters[2]] = '1'
            else:
                program[parameters[2]] = '0'
        if op == 8:
            if program[parameters[0]] == program[parameters[1]]:
                program[parameters[2]] = '1'
            else:
                program[parameters[2]] = '0'

        i += parametersLength + 1


def intCodeAdvance(program, input, step=0):
    result = None
    base = 0
    i = step
    program = program + (['0'] * 400000)
    while True:
        # print('op', program[i])
        op = int(program[i][-2:])
        if op == 99:
            return (result, True)

        if op == 1 or op == 2 or op == 7 or op == 8:
            parametersLength = 3
        if op == 3 or op == 4 or op == 9:
            parametersLength = 1
        if op == 5 or op == 6:
            parametersLength = 2

        modes = program[i][:-2].zfill(parametersLength)
        parameters = []
        for index, mode in enumerate(modes[::-1]):
            parameter = int(program[i + index + 1])
            if mode == '0':
                # position
                parameters.append(parameter)
            if mode == '1':
                # immediate
                parameters.append(i + index + 1)
            if mode == '2':
                # relative
                parameters.append(base + int(parameter))
        print(i, ' - op', program[i], parameters)

        if op == 1:
            program[parameters[2]] = str(
                int(program[parameters[0]]) + int(program[parameters[1]]))
        if op == 2:
            print(program[parameters[0]], program[parameters[1]], int(
                program[parameters[0]]) * int(program[parameters[1]]))
            program[parameters[2]] = str(
                int(program[parameters[0]]) * int(program[parameters[1]]))
        if op == 3:
            if len(input) == 0:
                return (result, False, i)
            program[parameters[0]] = str(input.pop(0))
        if op == 4:
            result = program[parameters[0]]
            # print('output', program[parameters[0]])

        if op == 5 and program[parameters[0]] != '0':
            i = int(program[parameters[1]])
            continue
        if op == 6 and program[parameters[0]] == '0':
            # print('6', parameters)
            i = int(program[parameters[1]])
            continue

        if op == 7:
            print(program[parameters[0]], program[parameters[1]])
            if int(program[parameters[0]]) < int(program[parameters[1]]):
                print('1')
                program[parameters[2]] = '1'
            else:
                print('0')
                program[parameters[2]] = '0'
        if op == 8:
            if int(program[parameters[0]]) == int(program[parameters[1]]):
                program[parameters[2]] = '1'
            else:
                program[parameters[2]] = '0'
        if op == 9:
            base = base + int(program[parameters[0]])
            print('base', base)
        i += parametersLength + 1
