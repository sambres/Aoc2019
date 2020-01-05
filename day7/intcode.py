
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
            program[parameters[0]] = str(input.pop())
        if op == 4:
            result = program[parameters[0]]
            # print('newinput', parameters[0], program[parameters[0]])

        if op == 5 and program[parameters[0]] != '0':
            # print('5', parameters)
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
