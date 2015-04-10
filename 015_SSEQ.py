"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""

import FASTA_Reader

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

RosalindFile = FASTA_Reader.FASTA_Reader('rosalind_sseq.txt')
RosalindFile.process_file()

FASTA_Dictionary = RosalindFile.getFASTA_dict()

sequence = FASTA_Dictionary[FASTA_Dictionary.keys()[1]]

subsequence = FASTA_Dictionary[FASTA_Dictionary.keys()[0]]

#In future solutions, need to remember that dictionary keys are ordered randomly
#so, if position of sequence in FASTA file is important, 
#Ex. Sequence listed first, subsequence listed second, that 
#positional info might change when the sequences are put in the FASTA dictionary.

Answer = FindSubSequence(sequence,subsequence)

for index in Answer:
    print index
