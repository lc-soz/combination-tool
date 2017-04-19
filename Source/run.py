import time
import fullLoop
import noReps
import os

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

seqMax = 5
values = 16, 18, 19, 20, 21, 24, 25, 30
targetValue = 251

optRuns = "c"
optTimes = 5
optPrint = 1

cls()
optChgVal = raw_input("Use all default values? (y/n) ")
optChgSet = raw_input("Use all default settings? (y/n) ")

if optChgVal == "n":
	seqMax = input("Sequence size: ")
	values = input("Values: ")
	targetValue = input("Target value: ")

if optChgSet == "n":
	optRuns = raw_input("Type: " + '\n' + "a = Combinations, don't consider order" + '\n' + "b = Permutation, consider order of elements" + '\n' + "c = Both" + '\n' + "Opt: ")
	optTimes = int(raw_input("Amount of runs: "))
	optPrint = int(raw_input("Full text (1), Only time (0): "))

cls()
print "Sequence size:   ", seqMax
print "Values:          ", values
print "Target value:    ", targetValue
print "Amount of runs:  ", optTimes
if optPrint == 1:
	print "Full text (Method | Sequences tested | Match sequences)"
	print "Time      (Method | Sequence size | Time used)\n"
else: print "Only time (Method | Sequence size | Time used)\n"
time.sleep(1)

for i in range(0, optTimes):
	if optRuns == 'a':
		noReps.noReps(seqMax, values, targetValue, optPrint)
	elif optRuns == 'b':
		fullLoop.fullLoop(seqMax, values, targetValue, optPrint)
	elif optRuns == 'c':
		noReps.noReps(seqMax, values, targetValue, optPrint)
		fullLoop.fullLoop(seqMax, values, targetValue, optPrint)
		print ''