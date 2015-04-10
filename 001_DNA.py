"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

#In retrospect creating the class below was a bit overkill for this problem.

class NucleotideCounter(object):
    def __init__(self, seq):
        self.A_count = 0
        self.G_count = 0
        self.C_count = 0
        self.T_count = 0
        self.seq = seq
        self.alreadyCounted = False
    def getCounts(self):
        return self.A_count, self.G_count, self.C_count, self.T_count
    def countNuc(self):
        if self.alreadyCounted == False:
            for nuc in self.seq:
                if nuc == 'A':
                    self.A_count += 1
                if nuc == 'G':
                    self.G_count += 1
                if nuc == 'C':
                    self.C_count += 1
                if nuc == 'T':
                    self.T_count += 1
            self.alreadyCounted = True
        else:
            print 'sequence has already been analyzed use .resetCounter() to reset all counts to 0.'
    def resetCounter(self):
        self.A_count = 0
        self.G_count = 0
        self.C_count = 0
        self.T_count = 0
        self.alreadyCounted = False
    def __str__(self):
        return 'A:' + str(self.A_count) + ' C:' + str(self.C_count) + ' G:' + str(self.G_count) + ' T:' + str(self.T_count)

RosalindFile = open('rosalind_dna.txt', 'r')
sequence = ""
for line in RosalindFile:
    sequence = line

Answer = NucleotideCounter(sequence)
Answer.countNuc()
print Answer
