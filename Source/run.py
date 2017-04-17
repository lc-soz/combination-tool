import math
import time

timeFrt = time.time()

seqMax = 13
values = [16, 18, 19, 20, 21, 24, 25, 30]
valuesQnt = len(values)
targetValue = 251

def seqTlValue(tbl):
	seqTlValue = 0
	for i in tbl:
		if i != None:
			seqTlValue += values[i]
	return seqTlValue

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

#print("========FULL LOOP========")
seqTest = [None] * seqMax
seqFinalSgl = []
lmt = valuesQnt
stg = -1
counterSgl = 0
timeSec = time.time()
while False:
	
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
		
		if seqTlValue(seqTest) == targetValue:
			seqFinalSgl.append(list(seqTest))
		#print("Sgl: ",seqTest)
		
		counterSgl += 1
	break

#print('\n' + "========LESS REPETITIONS========")

seqTest = [None] * seqMax
seqFinalLss = []
lmt = valuesQnt
stg = -1
counterLss = 0
timeThd = time.time()
while True:
	
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
				a = stg - 1
				while a < 0:
					seqTest[a] = seqTest[stg - 1]
					a += 1
				seqTest[stg] = seqTest[stg - 1]
			else:
				seqTest[stg - 1] += 1
				a = stg - 1
				while a < 0:
					seqTest[a] = seqTest[stg - 1]
					a += 1
				seqTest[stg] = seqTest[stg - 1]
			if seqTest[stg - 1] == lmt:
				stg -= 1
			else:
				stg = -1
				testOverFl = False
		
		if seqTlValue(seqTest) == targetValue:
			seqFinalLss.append(list(seqTest))
		#print("Lss: ", seqTest)
		
		counterLss += 1
	break

print(seqFinalSgl)
print('')
print(seqFinalLss)

print('\n' + "Full loop: " + str(counterSgl) + ': AFT: ' + str(seqTest) + " | " + str(len(seqFinalSgl)))
print('\n' + "Less rep.: " + str(counterLss) + ': AFT: ' + str(seqTest) + " | " + str(len(seqFinalLss)))


timeLst = time.time()
print('\n' + "Before runs: " + str(timeSec - timeSec))
print("Full loop:   " + str(timeThd - timeSec))
print("Less rep.:   " + str(timeLst - timeThd))
