"""Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
"""

import FASTA_Reader

def TransRatio(sequence1, sequence2):
    transitionCount = 0
    transversionCount = 0
    for i, nuc in enumerate(sequence1):
        if nuc == sequence2[i]:
            pass
        elif (nuc == 'A' and sequence2[i] == 'G') or (nuc == 'G' and sequence2[i] == 'A'):
            transitionCount+=1
        elif (nuc == 'C' and sequence2[i] == 'T') or (nuc == 'T' and sequence2[i] == 'C'):
            transitionCount+=1
        else:
            transversionCount+=1
    return float(transitionCount)/transversionCount

RosalindFile = FASTA_Reader.FASTA_Reader('rosalind_tran.txt')
RosalindFile.process_file()

Answer = RosalindFile.getFASTA_dict()

Ratio = TransRatio(Answer[Answer.keys()[0]], Answer[Answer.keys()[1]])

print Ratio
