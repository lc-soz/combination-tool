from config import *
import os
import time

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

cls()
optChg = raw_input("Use 'all', 'some' or 'no' default values/settings? (all/some/no) ")

if optChg == "no":
	seqMax = input("Sequence size: ")
	values = input("Values: ")
	targetMin = input("Min target value: ")
	targetMax = input("Max target value: ")
	optRuns = raw_input("Type: " + '\n' + "a = Combinations, don't consider order" + '\n' + "b = Permutation, consider order of elements" + '\n' + "c = Both" + '\n' + "Opt: ")
	optTimes = int(raw_input("Amount of runs: "))
	optPrint = raw_input("Full text (2), Time (1), Match sequences (0): (01;21;..)")
	optPrintSeq = raw_input("Print 'all' sequences or other amount? (all/int) ")
	optPrintSeqSize = raw_input("Print 'all' sizes or one specific? (all/int) ")

if optChg == "some":
	print "1. Sequence size\n2. Values\n3. Target Value (s)\n4. Runs options\n5. Amount of runs\n6. Print options\n7. Amount of sequences to be printed\n8. Sequences sizes to be printed"	
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
		if opt == '6': optPrint = raw_input("Full text (2), Time (1), Match sequences (0): (01;21;..)")
		if opt == '7': optPrintSeq = str(raw_input("Print 'all' sequences or other amount? (all/int) "))
		if opt == '8': optPrintSeqSize = str(raw_input("Print 'all' sizes or one specific? (all/int) "))

optPrtVal = []
for idx, val in enumerate(tuple(optPrint)):
	val = int(val)
	optPrtVal.append(val)
optPrint = tuple(optPrtVal)

print type(optPrint)
print optPrint
time.sleep(3)
cls()
print "         OPTIONS         ", "            VALUES"
print "Sequence size:           ", seqMax
print "Values:                  ", values
print "Min to Max target value: ", targetMin, " to ", targetMax
print "Amount of runs:          ", optTimes

print "\nPRINTED:"
print "Target Value: 'value'"
for idx, prt in enumerate(optPrint):
	if prt == 0:
		print optPrintSeq, "matching sequences,", "size:", optPrintSeqSize, ''
	elif prt == 1:
		print "Time      (Method | Sequence size | Time used)"
	elif prt == 2:
		print "Full text (Method | Sequences tested | Match sequences)"
print ""
time.sleep(0.5)