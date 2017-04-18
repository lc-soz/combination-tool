import time
import fullLoop
import noReps

seqMax = 6
values = [16, 18, 19, 20, 21, 24, 25, 30]
targetValue = 251

time.sleep(2)

for i in range(0, 5):

	noReps.noReps(seqMax, values, targetValue, 0)
	fullLoop.fullLoop(seqMax, values, targetValue, 0)
