import math

seqMax = 13
values = [16, 18, 19, 20, 21, 24, 25, 30]
valuesQnt = len(values)
targetValue = 251

# Amount of possible combinations with repetition per sequence size

math.factorial(valuesQnt)

seqQnt, seqQntSum = [0], 0
a = 1
while a <= seqMax:
	m = valuesQnt + a - 1
	seqQnt.append((math.factorial(m))/(math.factorial(m - a) * math.factorial(a)))
	a += 1

b = 0
while b <= seqMax:
	seqQntSum += seqQnt[b]
	print(str(b) + " = " + str(seqQnt[b]))
	b += 1
print("TOTAL = " + str(seqQntSum) + '\n')

# Table with all the possible sequences of a unitary value

seqSingleQnt = seqMax * valuesQnt
seqSingle = []
c = 0
while c < seqSingleQnt:
	seqSingleSize = (c % 13) + 1
	valueIndex = c / 13
	seqSingle.append([[values[valueIndex], seqSingleSize], values[valueIndex] * seqSingleSize])
	print(str(c) + "|" + str(seqSingleSize) + "|" + str(valueIndex))
	print(str(seqSingle) + '\n')
	c += 1


