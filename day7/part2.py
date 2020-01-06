from intcode import intCodeAdvance
from itertools import permutations
import time

start_time = time.time()

f = open("input", "r")
contents = f.read()
array = contents.split(',')


class Program:

    def __init__(self, name, phase):
        self.name = name
        self.phase = phase
        self.terminated = False
        self.step = 0
        self.output = 0
        self.input = [self.phase]
        self.commands = array.copy()

    def __repr__(self):
        return f'[{self.name}] T: {self.terminated}, step: {self.step}, input: {self.input}, output: {self.output}'

    def go(self, input):
        result = None
        self.input = self.input + input
        print('input', self.input)
        result = intCodeAdvance(self.commands, self.input, self.step)
        self.output = list(map(int,  result[0]))
        if result[1]:
            self.terminated = True
        else:
            self.step = result[2]


# phases = [[9, 8, 7, 6, 5]]
# phases = [[9, 7, 8, 5, 6]]
phases = list(map(list, permutations(map(lambda x: x + 5, range(5)), 5)))
# print(len(phases))
idealPhase = None
maxOutput = 0
for phase in phases:
    programs = []
    for index, thruster in enumerate(['A', 'B', 'C', 'D', 'E']):
        p = Program(thruster, phase[index])
        programs.append(p)

    output = [0]
    currentProgram = 0
    while programs[-1].terminated == False:
        program = programs[currentProgram]
        if program.terminated == False:
            # print('GO', program)
            program.go(output)
            # print('FINISH', program)
        # print(output)
        output = program.output
        currentProgram = (currentProgram + 1) % len(programs)

    # for index, thruster in enumerate(['A', 'B', 'C', 'D', 'E']):
    #     output = intCodeAdvance(array, [output, phase[index]])
    # print(phase, output)
    if int(output[-1]) > maxOutput:
        idealPhase = phase
        maxOutput = int(output[-1])

print('final', maxOutput, idealPhase)

print("--- %s seconds ---" % (time.time() - start_time))
