"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""


import copy
#import TestFindSharedMotif
import FASTA_Reader_faster 


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


RosalindFile = FASTA_Reader_faster.FASTA_Reader('rosalind_lcsm.txt')
RosalindFile.process_file()

Answers = sorted(RosalindFile.getFASTA_list())
print 'Answers'

matches = CompareTwoSeqs(Answers[0], Answers[1])
print 'Compared'

for seq in Answers[2:]:
    matches = CheckMatches(matches,seq)
print 'Checked'
print BestSolution(matches)

