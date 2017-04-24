from config import *

# Create function to print organized table on console
'''
>"head" will be a list or tuple of all the headers
>"content" will be a matrix, for exemple: 
- In a table with 2 colums
index 0: ["Sequence size", 22]
index 1: ["Values", (16, 18, 19, 20, 21, 24, 25, 30)]
This table will be: [["Sequence size", 22],  ["Values", (16, 18, 19, 20, 21, 24, 25, 30)]]
'''

def prtTbl(head, content):
#	for idx, val in enumerate(head):
#		print idx, val
	colAmount = len(head)
	colSizes = [0] * colAmount
	for idx, val in enumerate(content):
		print ""
		print idx, val
		for i in range(0, colAmount):
			valStr = str(val[i])
			if colSizes[i] < len(valStr):
				colSizes[i] = len(valStr)
				if (len(valStr) % 2) != 0:
					colSizes[i] += 1
			
				
	
	
	print colSizes
		
		
		
		
head = ["OPTIONS", "VALUES"]
content = [["Sequence size", seqMax],["Values", values],["Min to Max target value", str(str(targetMin) + " to " + str(targetMax))],["Amount of runs", optTimes]]
prtTbl(head, content)