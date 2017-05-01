def difSeq(lst, opt):
	# opt = 1: Order sequences by amount of unique values
	if opt == 1:
		lstTemp = lst
		repAmountLst = []
		for idxSeq, seq in enumerate(lstTemp):
			repAmount = len(seq)
			for idxValFst, valFst in enumerate(seq):
				for idxValSec, valSec in enumerate(seq):
					if valFst == valSec and idxValFst != idxValSec: repAmount -= 1
			repAmountLst.append(repAmount)
		lstOrder = [lstTemp for (repAmountLst, lstTemp) in sorted(zip(repAmountLst, lstTemp))]
		lstOrder = list(reversed(lstOrder))
		return lstOrder

			
lst = [[2,4,5,7],[5,5,6,9],[1,5,3,9],[7,9,3,7],[2,5,6,6],[4,4,4,2]]
opt = 1
difSeq(lst, opt)
