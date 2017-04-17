import math
import time

timeFrt = time.time()

seqMax = 2
values = [16, 18, 19, 20, 21, 24, 25, 30]
valuesQnt = len(values)
targetValue = 40

def seqSglTotalValue(val):
	seqSglTotalValue = 0
	for i in val:
		if i != None:
			seqSglTotalValue += values[i]
	return seqSglTotalValue

# Amount of possible combinations (order doesn't matter) with repetition per sequence size

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

# Combination of single sequences to match target value // Combination using the given values to match targetValue

seqTest = [None] * seqMax
seqFinalSgl = []
lmt = valuesQnt
ver = True
stg = -1
a = 0
timeSec = time.time()
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
			else:
				seqTest[stg - 1] += 1
			if seqTest[stg - 1] == lmt:
				stg -= 1
			else:
				stg = -1
				testOverFl = False		
		if seqSglTotalValue(seqTest) == targetValue:
			seqFinalSgl.append(list(seqTest))
		print(seqTest)		
		a += 1
	print('\n' + "Use values: " + str(a) + ': AFT: ' + str(seqTest) + " | " + str(len(seqFinalSgl)))
	print(seqFinalSgl)
	if (not(all(isinstance(item, int) for item in seqTest)) or sum(seqTest) == ((lmt - 1) * seqMax)):
		ver = False

timeLst = time.time()
print('\n' + "Before runs: " + str(timeSec - timeSec))
print("Use values:  " + str(timeLst - timeSec))
