import math
import time

timeFrt = time.time()

seqMax = 5
values = [1, 3, 7, 10]
valuesQnt = len(values)
targetValue = 10

def seqTotalSize(val, seqSgl):
	seqTotalSize = 0
	for i in val:
		if i != None:
			seqTotalSize += seqSgl[i][0][1]
	return seqTotalSize 

def seqTotalValue(val, seqSgl):
	seqTotalValue = 0
	for i in val:
		if i != None:
			seqTotalValue += seqSgl[i][1]
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

# Table with all the possible sequences of an unitary value order by: Values order > Size AND Size > Values order

seqSglQnt = seqMax * valuesQnt
seqSglVal = []
c = 0
while c < seqSglQnt:
	seqSglSize = (c % seqMax) + 1
	valuesIndex = c / seqMax
	seqSglVal.append([[values[valuesIndex], seqSglSize], values[valuesIndex] * seqSglSize])
	#print(str(c) + "|" + str(valuesIndex) + "|" + str(seqSglSize))
	#print(str(seqSglVal) + '\n')
	c += 1

seqSglSiz = []
c = 0
while c < seqSglQnt:
	seqSglSize = (c / valuesQnt) + 1
	valuesIndex = c % valuesQnt
	seqSglSiz.append([[values[valuesIndex], seqSglSize], values[valuesIndex] * seqSglSize])
	#print(str(c) + "|" + str(valuesIndex) + "|" + str(seqSglSize))
	#print(str(seqSglSiz) + '\n')
	c += 1

# Combination of single sequences to match target value

seqTest = [None] * seqMax
seqFinalVal = []
seqSglQnt = len(seqSglVal)
ver = True
stg = -1
a = 0
timeSec = time.time()
while ver == True:
	
	seqTest[-1] = -1
	testOverFl = False
	while (not(all(isinstance(item, int) for item in seqTest)) or sum(seqTest) < (len(seqSglVal) - 1) * seqMax):
		if seqTest[stg] <= seqSglQnt:
			seqTest[stg] += 1
		
		if seqTest[stg] == seqSglQnt:
			testOverFl = True
		
		while testOverFl:
			seqTest[stg] = 0
			if seqTest[stg - 1] == None:
				seqTest[stg - 1] = 0
			else:
				seqTest[stg - 1] += 1
			if seqTest[stg - 1] == seqSglQnt:
				stg -= 1
			else:
				stg = -1
				testOverFl = False		
		if seqTotalValue(seqTest, seqSglVal) == targetValue and seqTotalSize(seqTest, seqSglVal) <= seqMax:
			seqFinalVal.append(list(seqTest))	
		a += 1
	print("Full run: " + str(a) + ': AFT: ' + str(seqTest) + " | " + str(stg))
	if (not(all(isinstance(item, int) for item in seqTest)) or (sum(seqTest) == (len(seqSglVal) - 1) * seqMax)):
		ver = False

seqTest = [None] * seqMax
seqFinalSiz = []
lmt = len(seqSglSiz)
ver = True
stg = -1
a = 0
timeThd = time.time()
while ver == True:
	
	seqTest[-1] = -1
	testOverFl = False
	while (not(all(isinstance(item, int) for item in seqTest)) or sum(seqTest) < ((lmt - 1) * seqMax)):
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
		if seqTotalValue(seqTest, seqSglSiz) == targetValue and seqTotalSize(seqTest, seqSglSiz) <= seqMax:
			seqFinalSiz.append(list(seqTest))
		a += 1
	print("Limit size: " + str(a) + ': AFT: ' + str(seqTest) + " | " + str(stg))
	if (not(all(isinstance(item, int) for item in seqTest)) or sum(seqTest) == ((lmt - 1) * seqMax)):
		ver = False

timeLst = time.time()
print('\n' + "Before runs: " + str(timeSec - timeFrt))
print("Full run:    " + str(timeThd - timeSec))
print("Limit size:  " + str(timeLst - timeThd) + '\n')
