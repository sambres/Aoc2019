import math
import time
import re
start_time = time.time()

f = open("./input", "r")
contents = f.read().split('-')
min = contents[0]
max = contents[1]
regex = re.compile(r'\d*(\d)\1+')
print(min, max)

words = filter(lambda s: regex.match(s),
               map(lambda n: str(n),
                   range(int(min), int(max)))
               )

passwords = []
for number in words:
    correct = True
    numberMap = {}
    for index in range(len(number) - 1):
        if number[index] > number[index + 1]:
            correct = False
            break

    if correct and 2 in list(map(lambda c: number.count(c), number)):
        passwords.append(number)

print(passwords[0:10])

print(len(passwords))

print("--- %s seconds ---" % (time.time() - start_time))
