class FASTA_Reader(object):
    """This class reads FASTA files."""
    def __init__(self, file_name):
        self.first_entry = True
        self.FASTAfile = open(file_name, 'r')
        self.FASTA_list = []

    def process_file(self):
        #This part of the code reads from the FASTA file and adds strands to the GC_content.
        #The remove_spec method is once again used to remove any special characters or spaces.
        blankstr = ""
        FASTA_key_name = ""
        for line in self.FASTAfile:
            if line[0] == '>':
                if self.first_entry == True:
                    self.first_entry = False
                else:
                    blankstr = self.remove_spec(blankstr)
                    self.FASTA_list.append(blankstr)
                    blankstr = ""
            else:
                blankstr += line
        blankstr = self.remove_spec(blankstr)
        self.FASTA_list.append(blankstr)
        self.FASTAfile.close()
        
    def remove_spec(self, strand):
        for x in strand:
            if x != 'A' and x != 'G' and x != 'C' and x != 'T':
                strand = strand.replace(x, "")
        return strand

    def getFASTA_list(self):
        return self.FASTA_list
