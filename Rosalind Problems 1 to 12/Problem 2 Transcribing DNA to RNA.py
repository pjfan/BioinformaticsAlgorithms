"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

def TranscribeDNAtoRNA(sequence):
    output_RNA = ''
    for nuc in sequence:
        if nuc == 'T':
            output_RNA += 'U'
        else:
            output_RNA += nuc
    return output_RNA


RosalindFile = open('rosalind_rna.txt','r')
sequence = ''
for line in RosalindFile:
    sequence = line
print TranscribeDNAtoRNA(sequence)
