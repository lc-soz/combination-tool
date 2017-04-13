import math

seqMax = 13
values = [16, 18, 19, 20, 21, 24, 25, 30]
valuesQnt = len(values)

# Amount of possible combinations with repetition per sequence size

math.factorial(valuesQnt)

seqQnt, seqQntSum = [0], 0
i = 1
while i <= seqMax:
	m = valuesQnt + i - 1
	seqQnt.append((math.factorial(m))/(math.factorial(m - i) * math.factorial(i)))
	i += 1

a = 0
while a <= seqMax:
	seqQntSum += seqQnt[a]
	print(str(a) + " = " + str(seqQnt[a]))
	a += 1
print("TOTAL = " + str(seqQntSum))
