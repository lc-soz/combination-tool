import time
import fullLoop
import noReps
import os

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

seqMax = 9
values = 16, 18, 19, 20, 21, 24, 25, 30
targetMin = 260
targetMax = 265

optRuns = "a"
optTimes = 1
optPrint = 2

cls()
optChg = raw_input("Use 'all', 'some' or 'no' default values/settings? (all/some/no) ")

if optChg == "no":
	seqMax = input("Sequence size: ")
	values = input("Values: ")
	targetMin = input("Min target value: ")
	targetMax = input("Max target value: ")
	optRuns = raw_input("Type: " + '\n' + "a = Combinations, don't consider order" + '\n' + "b = Permutation, consider order of elements" + '\n' + "c = Both" + '\n' + "Opt: ")
	optTimes = int(raw_input("Amount of runs: "))
	optPrint = int(raw_input("Match sequences (2), Full text (1), Only time (0): "))
	
if optChg == "some":
	print "1. Sequence size\n2. Values\n3. Target Value (s)\n4. Runs options\n5. Amount of runs\n6. Print options"	
	optChgSome = raw_input("Please list all values/settings you want to change: ")

if 'optChgSome' in locals():
	for opt in optChgSome:
		if opt == '1': seqMax = input("Sequence size: ")
		if opt == '2': values = input("Values: ")
		if opt == '3':
			targetMin = input("Min target value: ")
			targetMax = input("Max target value: ")
		if opt == '4': optRuns = raw_input("Type: " + '\n' + "a = Combinations, don't consider order" + '\n' + "b = Permutation, consider order of elements" + '\n' + "c = Both" + '\n' + "Opt: ")
		if opt == '5': optTimes = int(raw_input("Amount of runs: "))
		if opt == '6': optPrint = int(raw_input("Match sequences (2), Full text (1), Only time (0): "))
	
cls()
print "Sequence size:           ", seqMax
print "Values:                  ", values
print "Min to Max target value: ", targetMin, " to ", targetMax
print "Amount of runs:          ", optTimes
if optPrint == 1:
	print "Full text (Method | Sequences tested | Match sequences)"
	print "Time      (Method | Sequence size | Time used)\n"
elif optPrint == 2:
	print "Match sequences"
	print "Time      (Method | Sequence size | Time used)\n"
elif optPrint == 0: print "Only time (Method | Sequence size | Time used)\n"
time.sleep(1)

for targetValue in range(targetMin, targetMax + 1):
	for i in range(0, optTimes):
		print "Target Value: ", targetValue
		if optRuns == 'a':
			noReps.noReps(seqMax, values, targetValue, optPrint)
		elif optRuns == 'b':
			fullLoop.fullLoop(seqMax, values, targetValue, optPrint)
		elif optRuns == 'c':
			noReps.noReps(seqMax, values, targetValue, optPrint)
			fullLoop.fullLoop(seqMax, values, targetValue, optPrint)
			print ''