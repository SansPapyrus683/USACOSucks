"""
ID: kevinsh4
TASK: fact4
LANG: PYTHON3
"""
with open('bigBigBigO.txt') as read:  # i just realized i made a sans reference
    theFact = int(read.read())

fiveCount, currFivePower = 0, 5

while theFact//currFivePower > 0:  # these two loops get how many zeroes there are in the factorial
    fiveCount += theFact//currFivePower
    currFivePower *= 5

twoZeroes = fiveZeroes = fiveCount
unitDigits = 1
for i in range(1, theFact + 1):
    while i % 5 == 0 and fiveZeroes > 0:
        i /= 5
        fiveZeroes -= 1

    while i % 2 == 0 and twoZeroes > 0:
        i /= 2
        twoZeroes -= 1

    unitDigits = (unitDigits * i) % 10

with open('outputs.txt', 'w') as written:
    written.write(str(int(unitDigits)) + '\n')
