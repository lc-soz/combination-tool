import time

def seqTlValue(tbl, values):
	seqTlValue = 0
	for i in tbl:
		if i != None:
			seqTlValue += values[i]
	return seqTlValue

def fullLoop(seqMax, values, targetValue, optPrint, optPrintSeq, optPrintSeqSize, optPrintSeqOrder):
	timeFst = time.time()
	seqTest = [None] * seqMax
	seqFinalSgl = []
	lmt = len(values)
	stg = -1
	counterSgl = 0
	
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
				else:
					seqTest[stg - 1] += 1
				if seqTest[stg - 1] == lmt:
					stg -= 1
				else:
					stg = -1
					testOverFl = False
	
			if seqTlValue(seqTest, values) == targetValue:
				seqFinalSgl.append(list(seqTest))
	
			counterSgl += 1
		break
		
	if optPrint != 0:
		print("Full Loop" + " | " + str(counterSgl) + " | " + str(len(seqFinalSgl)))

	timeLst = time.time()
	print("Full Loop | " + str(seqMax) + " | " + str(timeLst - timeFst))
