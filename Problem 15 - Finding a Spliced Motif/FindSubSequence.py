def FindSubSequence(sequence, subsequence):
	indices = []
	currentIndex = 0
	for subnuc in subsequence:
		for i, nuc in enumerate(sequence[currentIndex:]):
			if subnuc == nuc:
				indices.append(currentIndex+i+1)
				currentIndex += i+1
				break
			else:
				continue
	return indices

