def printList(lst, values, optPrintSeq, optPrintSeqSize):
	count = 1
	for seq in lst:
		seqPrint = []
		for val in seq:
			if val != None:
				seqPrint.append(values[val])

		if optPrintSeq == "all" and optPrintSeqSize == "all":
			print seqPrint
		elif optPrintSeq != "all" and optPrintSeqSize == "all":
			print seqPrint
			if count == int(optPrintSeq): break
			count += 1
		elif optPrintSeq == "all" and optPrintSeqSize != "all":
			if len(seqPrint) == int(optPrintSeqSize):
				print seqPrint
		elif optPrintSeq != "all" and optPrintSeqSize != "all":
			if len(seqPrint) == int(optPrintSeqSize):
				print seqPrint
				if count == int(optPrintSeq): break
				count += 1
