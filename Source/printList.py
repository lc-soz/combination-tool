def printList(lst, values, optPrintSeq, optPrintSeqSize):
	count = 0
	for seq in lst:
		seqPrint = []
		for val in seq:
			if val != None:
				seqPrint.append(values[val])
		
		if optPrintSeq == "all" and optPrintSeqSize == "all":
			print seqPrint
			
		elif optPrintSeq != "all" and optPrintSeqSize == "all":
			print seqPrint
			count += 1
			
		elif optPrintSeq == "all" and optPrintSeqSize != "all":
			if type(optPrintSeqSize) == int and len(seqPrint) == int(optPrintSeqSize):
				print seqPrint
			elif type(optPrintSeqSize) == list:
				for size in optPrintSeqSize:
					if len(seqPrint) == int(size):
						print seqPrint
						
		elif optPrintSeq != "all" and optPrintSeqSize != "all":
			if type(optPrintSeqSize) == int and len(seqPrint) == int(optPrintSeqSize):
				print seqPrint
				count += 1
			elif type(optPrintSeqSize) == list:
				for size in optPrintSeqSize:
					if len(seqPrint) == int(size):
						print seqPrint
						count += 1
						
		if count == int(optPrintSeq): break
 