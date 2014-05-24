"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

class FASTA_GC_Count(object):
    """This class reads FASTA files."""
    def __init__(self, file_name):
        self.first_entry = True
        self.FASTAfile = open(file_name, 'r')
        self.GC_dict = dict()
    def process_file(self):
        #This part of the code reads from the FASTA file and adds strands to the GC_content.
        #The remove_spec method is once again used to remove any special characters or spaces.
        blankstr = ""
        FASTA_key_name = ""
        for line in self.FASTAfile:
            if line[0] == '>':
                if self.first_entry == True:
                    self.first_entry = False
                    FASTA_key_name = line
                else:
                    blankstr = self.remove_spec(blankstr)
                    self.GC_dict[FASTA_key_name] = self.GC_calc(blankstr)
                    blankstr = ""
                    FASTA_key_name = line
            else:
                blankstr += line
        blankstr = self.remove_spec(blankstr)
        self.GC_dict[FASTA_key_name] = self.GC_calc(blankstr)
        
    def remove_spec(self, strand):
        for x in strand:
            if x != 'A' and x != 'G' and x != 'C' and x != 'T':
                strand = strand.replace(x, "")
        return strand

    def GC_calc(self,sequence):
        GC_count = 0
        for nuc in sequence:
            if nuc == 'G':
                GC_count += 1
            if nuc == 'C':
                GC_count += 1
        GC_content = float(GC_count)/len(sequence)
        return GC_content

    def getHighestGC(self):
        highestGCseq = sorted(self.GC_dict.keys(), key = self.GC_dict.__getitem__, reverse=True)[0]
        return 'Sequence: ' + highestGCseq[0:(len(highestGCseq)-1)] + ' GC content: ' + str(self.GC_dict[highestGCseq]*100)

x = FASTA_GC_Count('rosalind_gc.txt')
x.process_file()
print x.getHighestGC()
