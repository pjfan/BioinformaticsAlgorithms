"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

"""


def ReverseTranslatePos(prot_sequence):
	possibilities = 1
	for aa in prot_sequence:
		possibilities *= AAtoRNAnumber(aa)
		if possibilities > 1000000:
			possibilities = possibilities % 1000000
	return (possibilities*3) % 1000000

def AAtoRNAnumber(aa):
	if aa == 'F':
		return 2
	if aa == 'L':
		return 6
	if aa == 'S':
		return 6
	if aa == 'Y':
		return 2
	if aa == 'Stop':
		return 3
	if aa == 'C':
		return 2
	if aa == 'W':
		return 1
	if aa == 'P':
		return 4
	if aa == 'H':
		return 2
	if aa == 'Q':
		return 2
	if aa == 'R':
		return 6
	if aa == 'I':
		return 3
	if aa == 'M':
		return 1
	if aa == 'T':
		return 4
	if aa == 'N':
		return 2
	if aa == 'K':
		return 2
	if aa == 'V':
		return 4
	if aa == 'A':
		return 4
	if aa == 'D':
		return 2
	if aa == 'E':
		return 2
	if aa == 'G':
		return 4
	else:
		return 1


RosalindFile = open('rosalind_mrna.txt', 'r')
sequence = ''
for line in RosalindFile:
	sequence = line
print sequence

print ReverseTranslatePos(sequence)
