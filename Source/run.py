import time
import fullLoop
import noReps
import os

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

seqMax = 13
values = 16, 18, 19, 20, 21, 24, 25, 30
targetValue = 251

cls()
optChange = raw_input("Use all default values? (y/n) ")
if optChange == 'n':
	seqMax = input("Sequence size: ")
	values = input("Values: ")
	targetValue = input("Target value: ")
else: cls()
optRuns = raw_input("Type: " + '\n' + "a = Combinations, don't consider order" + '\n' + "b = Permutation, consider order of elements" + '\n' + "c = Both" + '\n' + "Opt: ")
optTimes = int(raw_input("Amount of runs: "))
optPrint = int(raw_input("Full text (1), Only time (0): "))

print ''
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