import math
import time
start_time = time.time()

f = open("input", "r")
contents = f.read()

array = []
for op in contents.split(','):
    array.append(int(op))

print(array)

array[1] = 12
array[2] = 2

i = 0
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

    i += 4
print(array)
print(array[0])

print("--- %s seconds ---" % (time.time() - start_time))
