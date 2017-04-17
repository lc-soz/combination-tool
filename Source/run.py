import math
import time

timeFrt = time.time()

seqMax = 5
values = [1, 3, 7, 10]
valuesQnt = len(values)
targetValue = 10

def seqTotalSize(val):
	seqTotalSize = 0
	for i in val:
		if i != None:
			seqTotalSize += seqSingle[i][0][1]
	return seqTotalSize 

def seqTotalValue(val):
	seqTotalValue = 0
	for i in val:
		if i != None:
			seqTotalValue += seqSingle[i][0][0] * seqSingle[i][0][1]
	return seqTotalValue

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

# Table with all the possible sequences of a unitary value order: Values original order and size / Size and values original order

seqSingleQnt = seqMax * valuesQnt
seqSingle = []
c = 0
while c < seqSingleQnt:
	seqSingleSize = (c % seqMax) + 1
	valuesIndex = c / seqMax
	seqSingle.append([[values[valuesIndex], seqSingleSize], values[valuesIndex] * seqSingleSize])
	#print(str(c) + "|" + str(valuesIndex) + "|" + str(seqSingleSize))
	#print(str(seqSingle) + '\n')
	c += 1

seqSingleOrder = []
c = 0
while c < seqSingleQnt:
	valuesIndex = (c % valuesQnt)
	seqSingleSize = (c / valuesQnt) + 1
	seqSingleOrder.append([[values[valuesIndex], seqSingleSize], values[valuesIndex] * seqSingleSize])
	print(str(c) + "|" + str(valuesIndex) + "|" + str(seqSingleSize))
	print(str(seqSingleOrder) + '\n')
	c += 1

# Combination of single sequences to match target value

seqTest = [None] * seqMax
seqFinal = []
seqSingleQnt = len(seqSingle)
ver = True
stg = -1
lmt = seqSingleQnt

a = 0
timeSec = time.time()
while ver == True:
	
	seqTest[-1] = -1
	testOverFl = False
	while (not(all(isinstance(item, int) for item in seqTest)) or sum(seqTest) < (len(seqSingle) - 1) * seqMax):
		if seqTest[stg] < lmt:
			seqTest[stg] += 1
		
		if seqTest[stg] == lmt:
			testOverFl = True
		
		while testOverFl:
			seqTest[stg] = 0
			if seqTest[stg - 1] == None:
				seqTest[stg - 1] = 0
				lmt -= valuesQnt
			else:
				seqTest[stg - 1] += 1
			if seqTest[stg - 1] == lmt:
				stg -= 1
			else:
				stg = -1
				testOverFl = False		
		a += 1
	print(str(a) + ': AFT: ' + str(seqTest) + " | " + str(stg))
	if (not(all(isinstance(item, int) for item in seqTest)) or (sum(seqTest) == (len(seqSingle) - 1) * seqMax)):
		ver = False

timeLst = time.time()
print(timeSec - timeFrt)
print(timeLst - timeSec)
