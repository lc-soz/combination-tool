from ui import *
import time
import fullLoop
import noReps

for targetValue in range(targetMin, targetMax + 1):
	for i in range(0, optTimes):
		print "Target Value:", targetValue
		if optRuns == 'a':
			noReps.noReps(seqMax, values, targetValue, optPrint, optPrintSeq, optPrintSeqSize, optPrintSeqOrder)
			print ''
		elif optRuns == 'b':
			fullLoop.fullLoop(seqMax, values, targetValue, optPrint, optPrintSeq, optPrintSeqSize, optPrintSeqOrder)
			print ''
		elif optRuns == 'c':
			noReps.noReps(seqMax, values, targetValue, optPrint, optPrintSeq, optPrintSeqSize, optPrintSeqOrder)
			fullLoop.fullLoop(seqMax, values, targetValue, optPrint, optPrintSeq, optPrintSeqSize, optPrintSeqOrder)
			print ''