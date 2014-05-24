import RevTransPos

RosalindFile = open('rosalind_mrna.txt', 'r')
sequence = ''
for line in RosalindFile:
	sequence = line
print sequence

print RevTransPos.ReverseTranslatePos(sequence)
