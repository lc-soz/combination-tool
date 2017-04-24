from config import *
import math

# Create function to print organized table on console
'''
>"head" will be a list or tuple of all the headers
>"data" will be a matrix, for example: 
- In a table with 2 colums
index 0: ["Sequence size", 22]
index 1: ["Values", (16, 18, 19, 20, 21, 24, 25, 30)]
This table will be: [["Sequence size", 22],  ["Values", (16, 18, 19, 20, 21, 24, 25, 30)]]
'''

def prtTbl(head, data):
#	for idx, val in enumerate(head):
#		print idx, val
	colAmount = len(head)
	colSizes = [0] * colAmount
	for idx, val in enumerate(data):
		for i in range(0, colAmount):
			valStr = str(val[i])
			if colSizes[i] < len(valStr):
				colSizes[i] = len(valStr) + 2
				if (len(valStr) % 2) == 1:
					colSizes[i] += 1
	
	# Vertical upper and lower line
	lineVertExtSize = colAmount - 1
	for size in colSizes:
		lineVertExtSize += size
	lineVertExt = "|" + "-" * lineVertExtSize + "|"
	
	# Vertical internal lines
	lineVertInt = ""
	for idx, size in enumerate(colSizes):
		if idx == 0:	lineVertInt += "|" + "-" * size
		else: 			lineVertInt += "+" + "-" * size
	lineVertInt += "|"
	
	# Header
	header = ""
	for idx, text in enumerate(head):
		headerSpaces = " " * ((colSizes[idx] - len(head[idx]))/2)
		if len(text) % 2 == 0:	header += "|" + headerSpaces + text + headerSpaces
		else:					header += "|" + headerSpaces + text + headerSpaces + " "
	header += "|"

	# Table content
	content = ""
	for line in data:
		for idx, col in enumerate(line):
			spaces = colSizes[idx] - len(str(col)) - 1
			content += "| " + str(col) + " " * spaces
		content += '|'
		if line != data[-1]:
			content += '\n'
	
	# Printing
	print lineVertExt
	print header
	print lineVertInt
	print content
	print lineVertExt
		
		
head = ["OPTIONS", "VALUES"]
data = [["Sequence size", seqMax],["Values", values],["Min to Max target value", str(str(targetMin) + " to " + str(targetMax))],["Amount of runs", optTimes]]
prtTbl(head, data)