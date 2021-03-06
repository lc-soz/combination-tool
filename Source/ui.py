from config import *
import os
import time
import printTbl

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

cls()
optChg = raw_input("Use 'all', 'some' or 'no' default values/settings? (all/some/no) ")

if optChg == "no":
	optChgDef = range(1,10)

if optChg == "some":
	print "1. Sequence size\n2. Values\n3. Target Value (s)\n4. Runs options\n5. Amount of runs\n6. Print options\n7. Amount of sequences to be printed\n8. Sequences sizes to be printed\n9. Print filtered/ordered by unique values in sequence"
	optChgDef = raw_input("Please list all values/settings you want to change: ")

if 'optChgDef' in locals():
	for opt in optChgDef:
		opt = str(opt)
		if opt == '1': seqMax = input("Sequence size: ")
		if opt == '2': values = input("Values: ")
		if opt == '3':
			targetMin = input("Min target value: ")
			targetMax = input("Max target value: ")
		if opt == '4': optRuns = raw_input("Type: " + '\n' + "a = Combinations, don't consider order" + '\n' + "b = Permutation, consider order of elements" + '\n' + "c = Both" + '\n' + "Opt: ")
		if opt == '5': optTimes = int(raw_input("Amount of runs: "))
		if opt == '6': optPrint = raw_input("Full text (2), Time (1), Match sequences (0): (01;21;..)")
		if opt == '7': optPrintSeq = str(raw_input("Print 'all' sequences or other amount? (all/int) "))
		if opt == '8': optPrintSeqSize = str(raw_input("Print 'all' sizes, a specific one or a list? (all/int/'1,2;3,5,8;...') "))
		if opt == '9': optPrintSeqOrder = str(raw_input("Print ordered by script (0) or by amount of unique values (1)?"))

if optPrintSeqSize != "all":
	optPrintSeqSizeChar = ""
	optPrintSeqSizeTemp = []
	for char in optPrintSeqSize:
		if char != ",":
			optPrintSeqSizeChar += char
		else:
			optPrintSeqSizeTemp.append(int(optPrintSeqSizeChar))
			optPrintSeqSizeChar = ""
	if optPrintSeqSizeChar != "" and optPrintSeqSizeTemp != []:
		optPrintSeqSizeTemp.append(int(optPrintSeqSizeChar))
		optPrintSeqSize = optPrintSeqSizeTemp
	else: optPrintSeqSize = int(optPrintSeqSize)

optPrtVal = []
for idx, val in enumerate(tuple(optPrint)):
	val = int(val)
	optPrtVal.append(val)
optPrint = tuple(optPrtVal)

cls()

optPrintSeqOrder = int(optPrintSeqOrder)
if optPrintSeqOrder == 0: optPrintSeqOrderDisplay = "Original"
if optPrintSeqOrder == 1: optPrintSeqOrderDisplay = "Amount of unique values"

head = ["OPTIONS", "VALUES"]
data = [["Sequence size", seqMax],["Values", values],["Min to Max target value", str(str(targetMin) + " to " + str(targetMax))],["Amount of runs", optTimes],["Order", optPrintSeqOrderDisplay]]
printTbl.prtTbl(head, data)

print "\nPRINTED:"
print "Target Value: 'value'"
for idx, prt in enumerate(optPrint):
	if prt == 0:
		print optPrintSeq, "matching sequences,", "size(s):", optPrintSeqSize, ''
	elif prt == 1:
		print "Time      (Method | Sequence size | Time used)"
	elif prt == 2:
		print "Full text (Method | Sequences tested | Match sequences)"
print ""
time.sleep(0.5)