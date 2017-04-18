# Amount of possible combinations (order doesn't matter) with repetition per sequence size

math.factorial(valuesQnt)

seqQnt, seqQntSum = [0], 0
a = 1
while a <= seqMax:
	m = valuesQnt + a - 1
	seqQnt.append((math.factorial(m))/(math.factorial(m - a) * math.factorial(a)))
	a += 1

b = 0
while b <= seqMax:
	seqQntSum += seqQnt[b]
	#print(str(b) + " = " + str(seqQnt[b]))
	b += 1
#print("TOTAL = " + str(seqQntSum) + '\n')
