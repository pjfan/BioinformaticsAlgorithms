"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement, "sc", of s.
"""
def complementDNA(sequence):
    complementary_seq = ''
    for nuc in sequence:
        if nuc == 'T':
            complementary_seq += 'A'
        if nuc == 'G':
            complementary_seq += 'C'
        if nuc == 'A':
            complementary_seq +=  'T'
        if nuc == 'C':
            complementary_seq += 'G'
    return complementary_seq[::-1]

RosalindFile = open('rosalind_revc.txt','r')
sequence = ''
for line in RosalindFile:
    sequence = line
print complementDNA(sequence)
        
