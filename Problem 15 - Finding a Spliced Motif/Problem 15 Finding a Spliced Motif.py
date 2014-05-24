import FASTA_Reader
import FindSubSequence

RosalindFile = FASTA_Reader.FASTA_Reader('rosalind_sseq.txt')
RosalindFile.process_file()

FASTA_Dictionary = RosalindFile.getFASTA_dict()

sequence = FASTA_Dictionary[FASTA_Dictionary.keys()[1]]

subsequence = FASTA_Dictionary[FASTA_Dictionary.keys()[0]]

#In future solutions, need to remember that dictionary keys are ordered randomly
#so, if position of sequence in FASTA file is important, 
#Ex. Sequence listed first, subsequence listed second, that 
#positional info might change when the sequences are put in the FASTA dictionary.

Answer = FindSubSequence.FindSubSequence(sequence,subsequence)

for index in Answer:
	print index
