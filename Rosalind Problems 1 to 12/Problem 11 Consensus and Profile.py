"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return
any one of them.)
"""
import numpy as np

class ConsensusMtrx(object):
    """A class for keeping track of the profile matrix for a set of DNA strands"""
    def __init__(self, strandLength=5):
        self.strandLength = strandLength
        self.table = np.zeros((4, strandLength))
    def add(self, strand):
        for i, x in enumerate(strand):
            if x == 'A':
                self.table[0,i] += 1
            if x == 'G':
                self.table[1,i] += 1
            if x == 'C':
                self.table[2,i] += 1
            if x == 'T':
                self.table[3,i] += 1
    def format_array_ans(self, array_ans):
        blankstr = ""
        for x in array_ans:
            blankstr += str(int(x))
            blankstr += " "
        return blankstr
    def __str__(self):
        ConsensusStr = ""
        for y in xrange(self.strandLength):
            most_common_nuc = np.argmax(self.table[:,y])
            if most_common_nuc == 0:
                ConsensusStr += "A"
            if most_common_nuc == 1:
                ConsensusStr += "G"
            if most_common_nuc == 2:
                ConsensusStr += "C"
            if most_common_nuc == 3:
                ConsensusStr += "T"
        return ConsensusStr + "\n" + "A: " + self.format_array_ans(self.table[0,:]) + "\n" + "G: " + self.format_array_ans(self.table[1,:]) + "\n" + "C: " + self.format_array_ans(self.table[2,:]) + "\n" + "T: " + self.format_array_ans(self.table[3,:])


class FASTA_reader(object):
    """This class reads FASTA files and encapsulates a ConsensusMtrx object representing
    the consensus matrix for that file."""
    def __init__(self, file_name):
        self.first_entry = True
        self.FASTAfile = open(file_name, 'r+')

        #The following code creates a new ConsensusMtrx object with the same
        #length as the DNA strand length. The remove_spec is used to remove any special characters or spaces.

        start_end_counter = 0
        firstStrand = ""

        for line in self.FASTAfile:
            if line[0] == '>':
                start_end_counter += 1
                continue
            if start_end_counter == 2:
                break
            firstStrand += line

        firstStrand = self.remove_spec(firstStrand)
        self.matrix = ConsensusMtrx(len(firstStrand))
        self.FASTAfile.close()
        self.FASTAfile = open(file_name, 'r+')

    def process_file(self):
        #This part of the code reads from the FASTA file and adds strands to the consensus matrix.
        #The remove_spec method is once again used to remove any special characters or spaces.
        blankstr = ""
        for line in self.FASTAfile:
            if line[0] == '>':
                if self.first_entry == True:
                    self.first_entry = False
                    continue
                else:
                    blankstr = self.remove_spec(blankstr)
                    self.matrix.add(blankstr)
                    blankstr = ""
            else:
                blankstr += line
        blankstr = self.remove_spec(blankstr)
        self.matrix.add(blankstr)
        self.first_entry = True

        
    def remove_spec(self, strand):
        for x in strand:
            if x != 'A' and x != 'G' and x != 'C' and x != 'T':
                strand = strand.replace(x, "")
        return strand

    def __str__(self):
        return str(self.matrix)

    def getConsensusMtrx(self):
        return self.matrix

answer = FASTA_reader('rosalind_cons.txt')
answer.process_file()
print answer
