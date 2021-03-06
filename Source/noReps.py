import time
import printList

def seqTlValue(tbl, values):
	seqTlValue = 0
	for i in tbl:
		if i != None:
			seqTlValue += values[i]
	return seqTlValue
		
def noReps(seqMax, values, targetValue, optPrint, optPrintSeq, optPrintSeqSize, optPrintSeqOrder):
	timeFst = time.time()
	seqTest = [None] * seqMax
	seqFinalLss = []
	lmt = len(values)
	stg = -1
	counterLss = 0

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
	
			if seqTlValue(seqTest, values) == targetValue:
				seqFinalLss.append(list(seqTest))
	
			counterLss += 1
		break
	timeLst = time.time()
	for idx, prt in enumerate(optPrint):
		if prt == 0:
			printList.printList(seqFinalLss, values, optPrintSeq, optPrintSeqSize, optPrintSeqOrder)
		elif prt == 1:
			print("Less Rep  | " + str(seqMax) + " | " + str(timeLst - timeFst))
		elif prt == 2:
			print("Less Rep " + " | " + str(counterLss) + " | " + str(len(seqFinalLss)))