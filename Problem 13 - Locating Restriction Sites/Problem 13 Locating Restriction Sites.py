
import RevPalindromeFind
import FASTA_Reader

RosalindFile = FASTA_Reader.FASTA_Reader('rosalind_revp.txt')

RosalindFile.process_file()

FASTA_dict = RosalindFile.getFASTA_dict()
print FASTA_dict
sequence = FASTA_dict[FASTA_dict.keys()[0]]

for x in xrange(4,14,2):
	Answer = RevPalindromeFind.findPalindromes(sequence, x)
	for key in Answer.keys():
		print str(key) + " " + str(Answer[key])
