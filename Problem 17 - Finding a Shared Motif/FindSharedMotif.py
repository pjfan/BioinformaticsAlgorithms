import copy

def CompareTwoSeqs(sequence1, sequence2):
	matches = []
	for length in xrange(len(sequence1)):
		for index in xrange(len(sequence1)):
			#+1 is added so length = 0 does not occur
			if (index+length+1) > len(sequence1):
				break
			if sequence1[index:index+length+1] in matches:
				break
			if IsItInHere(sequence1[index:index+length+1], sequence2):
				matches.append(sequence1[index:index+length+1])
	return matches

def IsItInHere(sub_seq, sequence):
	for x in xrange(len(sequence)):
		if sequence[x:x+len(sub_seq)] == sub_seq:
			return True
	return False

def CheckMatches(matches, sequence):
	matches_check = copy.copy(matches)
	for seq in matches:
		if IsItInHere(seq, sequence):
			continue
		else:
			matches_check.remove(seq)
	return matches_check

def BestSolution(matches):
	best = ''
	for seq in matches:
		if len(seq) > len(best):
			best = seq
	return best
	